import logging
import dric
import cv2

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('camera_id', help='camera id to capture')
parser.add_argument('video_output', help='directory for the generated video files')
parser.add_argument('--fps', type=float, default=10.0, help='number of frames per second')
parser.add_argument('--video_interval', '-i', type=int, default=60*10, help='interval for a video in seconds')
parser.add_argument('--show', '-s', action='store_true', help='number of frames per second')
args = parser.parse_args()

dric.set_log_level(logging.DEBUG)
platform = dric.connect()


from collections import namedtuple
class Resolution(namedtuple('Resolution', 'width height')):
    def __repr__(self):
        return '%d x %d' % self

class Camera:
    logger = logging.getLogger("dric.camera")

    def __init__(self, id, vcap):
        self.id = id
        self.vcap = vcap

    def release(self):
        self.vcap.release()

    @property
    def size(self):
        return Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                            int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    def capture(self):
        ret, frame = self.vcap.read()
        if ret:
            return frame
        else:
            return None

    def __str__(self):
        return '{0}[{1}]'.format(type(self).__name__, self.id)

    @classmethod
    def capture(cls, camera_id, fps, proc, show_image=False):
        interval = max(round(1000.0 / fps) - 5, 1)

        vcap = dric.video_server().get_camera(camera_id)
        camera = Camera(camera_id, vcap)

        try:
            Camera.logger.info('start capturing camera={0}, fps={1}'.format(camera, fps))
            proc.on_capture_started(camera)
            while ( 1 ):
                frame = camera.capture()
                if frame is None: break

                import time
                ts = time.time()
                if Camera.logger.isEnabledFor(logging.DEBUG):
                    Camera.logger.info('capture a frame from {0}, ts={1}'.format(camera, ts))

                if show_image:
                    cv2.imshow(camera.id, frame)
                    if cv2.waitKey(interval) & 0xFF == ord('q'): break
                if proc.on_captured(camera, frame, ts) == False:
                    Camera.logger.info('client stopped capturing: camera=' + camera)
                    break
        finally:
            proc.on_capture_stopped(camera)
            camera.release()

class VideoCreater:
    def __init__(self, output_dir, fps, interval):
        self.output_dir = output_dir
        self.fps = fps
        self.interval = interval

    def on_capture_started(self, camera):
        self.writer = None

    def on_captured(self, camera, frame, ts):
        if not self.writer:
            self.writer = self.__open_video_writer(ts)
        elif (ts - self.start_ts) >= self.interval:
            self.writer.release()
            self.writer = self.__open_video_writer(ts)
        self.writer.write(frame)

    def on_capture_stopped(self, camera):
        if self.writer:
            self.writer.release()
            self.writer = None

    def __open_video_writer(self, camera, ts):
        self.start_ts = ts

        import os.path
        video_file = os.path.join(self.output_dir, '%s_%s.avi' % (camera.id, int(self.start_ts)))
        return cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*"DIVX"), self.fps, camera.size)

creater = VideoCreater(args.camera_id, args.video_output, args.fps, args.video_interval)
Camera.capture(args.camera_id, args.fps, creater, args.show)
dric.disconnect()
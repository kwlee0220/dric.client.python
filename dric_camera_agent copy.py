# import logging
import dric
import cv2

class BBoxObjectTracker:
    def __init__(self, ds, output_dir, interval):
        self.ds = ds
        self.output_dir = output_dir
        self.interval = interval
        self.ds_writer = None
        self.video_writer = None

    def on_capture_started(self, camera):
        self.ds_writer = self.ds.open_writer()
        self.ds_writer.__enter__()

    def on_captured(self, camera, image, ts):
        if self.output_dir is not None:
            if not self.video_writer:
                self.video_writer = self.__open_video_writer(camera, ts)
            elif (ts - self.start_ts) >= self.interval:
                self.video_writer.release()
                self.video_writer = self.__open_video_writer(camera, ts)
            self.video_writer.write(image)

        bstr = dric.to_bstring_from_mat(image)
        rec = dric.Record(self.ds.record_schema, (camera.id, bstr, ts))
        self.ds_writer.write(rec)

    def on_capture_stopped(self, camera):
        if self.video_writer is not None:
            self.video_writer.release()
            self.video_writer = None
        if self.ds_writer is not None:
            self.ds_writer.close()
            self.ds_writer.__exit__(None, None, None)

    def __open_video_writer(self, camera, ts):
        self.start_ts = ts

        import time
        dt_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(ts / 1000.0))
        fname = '{0}_{1}.avi'.format(camera.id, dt_str)

        from pathlib import Path
        video_path = Path(self.output_dir) / fname
        video_path.parent.mkdir(parents=True, exist_ok=True)
        logger.info('create a video file: {0}'.format(video_path))
        return cv2.VideoWriter(str(video_path), cv2.VideoWriter_fourcc(*"DIVX"), 30, camera.size)
        # return cv2.VideoWriter(str(video_path), cv2.VideoWriter_fourcc(*"DIVX"), camera.fps, camera.size)

def run(capture_fact, tracker, loop, show_image):
    try:
        camera = capture_fact()

        size = camera.size
        import numpy as np
        empty_image = np.zeros((size.height, size.width, 3), np.uint8)
        cv2.putText(empty_image, 'monitoring {0}...'.format(camera.id), (30, int(size.height/2)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255,255,255), 2)

        tracker.on_capture_started(camera)
        while ( 1 ):
            sleep_millis, frame = camera.capture()
            if frame is not None:
                started = dric.current_millis()
                tracker.on_captured(camera, frame, started)
                if show_image:
                    cv2.imshow(camera.id, frame)
                else:
                    cv2.imshow(camera.id, empty_image)
    
                elapsed = dric.current_millis() - started
                sleep_millis = max(sleep_millis - elapsed - 3, 1)
                code = cv2.waitKey(sleep_millis) & 0xFF
                if code == ord('q'):
                    break
                elif code == ord('v'):
                    show_image = not show_image
            elif loop:
                camera.release()
                camera = capture_fact()
            else: break
    finally:
        tracker.on_capture_stopped(camera)
        camera.release()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('camera_id', help='camera id to capture')
    parser.add_argument('--output_dir', '-o', type=str, required=False, help='directory for created video files')
    parser.add_argument('--video_file', '-f', type=str, help='video file path')
    parser.add_argument('--video_interval', '-i', type=str, default="1h", help='interval for a video in seconds')
    parser.add_argument('--fps', type=float, default=10.0, help='number of frames per second')
    parser.add_argument('--loop', '-l', action='store_true', help='re-start to play at the end of the play')
    parser.add_argument('--show', '-s', action='store_true', help='number of frames per second')
    parser.add_argument('--topic', '-t', type=str, default='dric/camera_frames', help='target topic name')
    args = parser.parse_args()

    import logging
    logger = logging.getLogger("dric.camera_agent")
    logger.setLevel(logging.INFO)
    # logger.addHandler(logging.StreamHandler())

    dric.connect()
    try :
        topic = dric.get_dataset('topics/{0}'.format(args.topic))
        tracker = BBoxObjectTracker(topic, args.output_dir, dric.parse_duration(args.video_interval))

        if args.video_file:
            def create_video_player():
                return dric.VideoPlayer(args.camera_id, args.video_file)
            capture_fact = create_video_player
        else:
            def create_video_player():
                return dric.get_camera(args.camera_id, args.fps)
            capture_fact = create_video_player

        run(capture_fact, tracker, args.loop, args.show)
    finally:
        dric.disconnect()

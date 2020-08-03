import logging
import dric
import cv2

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('camera_id', help='camera id to capture')
parser.add_argument('video_file', help='target video file path')
parser.add_argument('--loop', '-l', action='store_true', help='re-start to play at the end of the play')
parser.add_argument('--show', '-s', action='store_true', help='number of frames per second')
args = parser.parse_args()

from collections import namedtuple
class Resolution(namedtuple('Resolution', 'width height')):
    def __repr__(self):
        return '%d x %d' % self
        
import time
class VideoPlayer:
    logger = logging.getLogger("dric.video")

    def __init__(self, id, file):
        self.id = id
        self.file = file
        self.vcap = cv2.VideoCapture(file)
        self.pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
        self.ts = time.time()

    def release(self):
        self.vcap.release()

    @property
    def size(self):
        return Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                            int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    def read(self):
        ret, frame = self.vcap.read()
        if ret:
            pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
            ts = time.time()
            idle_ts = (pos - self.pos) - (ts - self.ts)
            self.pos = pos
            self.ts = ts
            if idle_ts > 1:
                if cv2.waitKey(int(idle_ts)) & 0xFF == ord('q'):
                    return None
            return frame
        else:
            return None

    def __str__(self):
        return '{0}[{1}]'.format(type(self).__name__, self.id)

    @classmethod
    def play(cls, id, file, proc, show_image=False):
        player = VideoPlayer(id, file)
        try:
            cls.logger.info('start reading a video file=%s' % file)
            proc.on_capture_started(player)
            while ( 1 ):
                frame = player.read()
                if frame is None: break

                import time
                ts = time.time()
                if cls.logger.isEnabledFor(logging.DEBUG):
                    cls.logger.info('capture a frame from {0}, ts={1}'.format(player, ts))

                if show_image:
                    cv2.imshow(id, frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'): break
                if proc.on_captured(player, frame, ts) == False:
                    cls.logger.info('client stopped capturing: player=' + player)
                    break
        finally:
            proc.on_capture_stopped(player)
            player.release()


class BBoxObjectTracker:
    def __init__(self): pass

    def on_capture_started(self, player):
        pass

    def on_captured(self, player, frame, ts):
        pass

    def on_capture_stopped(self, player):
        pass

dric.set_log_level(logging.DEBUG)
platform = dric.connect()
VideoPlayer.play(args.camera_id, args.video_file, BBoxObjectTracker(), args.show)
dric.disconnect()
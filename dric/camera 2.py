import logging
import cv2
import threading
from .utils import current_millis

logger = logging.getLogger("dric.video")

from collections import namedtuple
class Resolution(namedtuple('Resolution', 'width height')):
    def __repr__(self):
        return '%d x %d' % self

from enum import Enum
class State(Enum):
    CLOSED = 1
    OPEN = 2
    CLOSING = 3
class Camera:
    def __init__(self, id, fps):
        self.id = id
        self.fps = fps
        self.interval = int(round(1000 / fps))
        self.vcap = None
        self.size = None

    def start(self):
        from .client import video_server
        self.vcap = video_server().get_camera(self.id)
        self.size = Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    def stop(self):
        self.release()

    def release(self):
        self.vcap.release()
        self.vcap = None
        self.size = None

    def capture(self):
        started = current_millis()
        ret, frame = self.vcap.read()
        if ret:
            elapsed = current_millis() - started
            sleep_millis = self.interval - elapsed
            return (sleep_millis,  frame)
        else:
            return (-1, None)

    def __str__(self):
        return '{0}[{1},{2}]'.format(type(self).__name__, self.id, str(self.size))

class VideoPlayer:
    def __init__(self, id, file, loop):
        self.id = id
        self.file = file
        self.loop = loop
        self.vcap = cv2.VideoCapture(file)
        self.fps = self.vcap.get(cv2.CAP_PROP_FPS)
        self.size = Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.last_pos = 0
        self.last_interval = 0

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, track_back):
        self.release()
        return False
    def release(self):
        self.vcap.release()

    def capture(self):
        started = current_millis()
        ret, frame = self.vcap.read()
        if not ret:     # if end-of-video
            if not self.loop:
                return (0, None)
            else:
                self.vcap.release()
                self.vcap = cv2.VideoCapture(self.file)
                ret, frame = self.vcap.read()
                pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
        else:
            pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
            self.last_interval = int(pos - self.last_pos)

        elapsed = current_millis() - started
        sleep_millis = self.last_interval - elapsed
        self.last_pos = pos
        return (sleep_millis, frame)

    def __str__(self):
        return '{0}[{1},{2}]'.format(type(self).__name__, self.id, str(self.size))
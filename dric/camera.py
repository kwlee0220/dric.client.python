import logging
import cv2
import time
from .utils import current_millis

logger = logging.getLogger("dric.video")

from collections import namedtuple
class Resolution(namedtuple('Resolution', 'width height')):
    def __repr__(self):
        return '%d x %d' % self

from abc import ABC, abstractmethod
class ImageSource(ABC):
    def __init__(self, id, size):
        self.id = id
        self.size = size        # Resolution

    @property
    @abstractmethod
    def fps(self): pass

    @abstractmethod
    def capture(self): pass     # (sleep_millis, frame)

    def __str__(self):
        return '{0}[{1},{2}]'.format(type(self).__name__, self.id, str(self.size))

class VideoCaptureSource(ImageSource):
    def __init__(self, id, vcap):
        super().__init__(id, Resolution(int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                        int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        self.vcap = vcap

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, track_back):
        self.release()
        return False
    def release(self):
        self.vcap.release()

class Camera(VideoCaptureSource):
    def __init__(self, id, vcap, fps):
        super().__init__(id, vcap)
        self._fps = fps
        self.interval = 1.0 / fps

    @property
    def fps(self):
        return self._fps

    def capture(self):
        started = current_millis()
        ret, frame = self.vcap.read()
        if ret:
            sleep_millis = self.interval - current_millis()
            return (sleep_millis,  frame)
        else:
            return (0, None)

class VideoPlayer(VideoCaptureSource):
    def __init__(self, id, file):
        vcap = cv2.VideoCapture(file)
        super().__init__(id, vcap)
        self.file = file
        self._fps = vcap.get(cv2.CAP_PROP_FPS)
        self.last_pos = 0

    @property
    def fps(self):
        return self._fps

    def capture(self):
        started = current_millis()
        ret, frame = self.vcap.read()
        if ret:
            elapsed = current_millis() - started
            pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
            sleep_millis = int(round(pos - self.last_pos - elapsed))
            self.last_pos = pos
            return (sleep_millis, frame)
        else:
            return (0, None)
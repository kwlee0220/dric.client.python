import logging
import cv2

logger = logging.getLogger("dric.video")

from collections import namedtuple
class Resolution(namedtuple('Resolution', 'width height')):
    def __repr__(self):
        return '%d x %d' % self

from abc import ABC, abstractmethod
class ImageSource(ABC):
    def __init__(self, id, size):
        self.id = id
        self.size = size

    @abstractmethod
    def capture(self): pass

class Camera(ImageSource):
    def __init__(self, id, vcap):
        self._id = id
        self.vcap = vcap
        self._size = Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, track_back):
        self.release()
        return False
    def release(self):
        self.vcap.release()

    @property
    def id(self):
        return self._id

    @property
    def size(self):
        return self._size

    def capture(self):
        ret, frame = self.vcap.read()
        if ret:
            return frame
        else:
            return ret

    def __str__(self):
        return '{0}[{1},{2}]'.format(type(self).__name__, self.id, str(self.size))

class VideoPlayer(ImageSource):
    def __init__(self, id, file):
        self._id = id
        self.file = file
        self.vcap = cv2.VideoCapture(file)
        self.pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
        self.ts = time.time()

    @property
    def id(self):
        return self._id

    @property
    def size(self):
        return self._size
        self._size = Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    def release(self):
        self.vcap.release()

    def read(self):
        ret, frame = self.vcap.read()
        if ret:
            pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
            ts = time.time()
            idle_ts = int((pos - self.pos) - (ts - self.ts) - 10)
            self.pos = pos
            self.ts = ts
            if idle_ts > 5:
                if cv2.waitKey(idle_ts) & 0xFF == ord('q'):
                    return None
            return frame
        else:
            return None
import logging
import cv2
import threading
from .utils import current_millis, parse_datetime_millis

logger = logging.getLogger("dric.video")

from collections import namedtuple
class Resolution(namedtuple('Resolution', 'width height')):
    def __repr__(self):
        return '%d x %d' % self

class Playback:
    def __init__(self, id, start_time, stop_time):
        self.id = id
        self.start_time = start_time
        self.stop_time = stop_time
        self.started = parse_datetime_millis(start_time)

        from .client import video_server
        stream = video_server().get_playback_stream(id, start_time, stop_time)
        self.vcap = cv2.VideoCapture(stream.rtsp_url)
        self.size = Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    def release(self):
        self.vcap.release()

    def capture(self):
        ret, frame = self.vcap.read()
        if ret:
            pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
            return (frame, self.started + pos)
        else:
            return (None, -1)

    def __str__(self):
        return '{0}[camera={1}, size={2}, interval={3} - {4}]'.format(type(self).__name__, self.id, str(self.size),
                                                                         self.start_time, self.stop_time)

class VideoPlayer:
    def __init__(self, id, file, start_ts):
        self.id = id
        self.file = file
        self.vcap = cv2.VideoCapture(file)
        self.size = Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.start_ts = start_ts

    def release(self):
        self.vcap.release()

    def capture(self):
        ret, frame = self.vcap.read()
        if ret:
            pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
            return (frame, self.start_ts + pos)
        else:
            return (None, -1)

    def __str__(self):
        return '{0}[{1},{2}]'.format(type(self).__name__, self.id, str(self.size))
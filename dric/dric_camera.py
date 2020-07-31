from collections import namedtuple
import cv2

class Resolution(namedtuple('Resolution', 'width height')):
    def __repr__(self):
        return '%d x %d' % self

class ImageProcessor:
    def on_capture_started(self, camera):
        raise NotImplementedError
    def on_captured(self, camera, frame):
        raise NotImplementedError
    def on_capture_stopped(self, camera):
        raise NotImplementedError

class Camera:
    def __init__(self, id, vcap):
        self.id = id
        self.vcap = vcap

    def __getattr__(self, name):
        if name == 'resolution':
            return Resolution(int(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    @classmethod
    def capture(cls, camera_id, fps, proc, show_image=False):
        interval = max(round(1000.0 / fps) - 10, 1)

        from .client import assert_platform
        vcap = assert_platform().video_server().get_camera(camera_id)
        camera = Camera(camera_id, vcap)
        try:
            proc.on_capture_started(camera)
            while ( 1 ):
                ret, frame = vcap.read()
                if not ret: break
                if show_image:
                    cv2.imshow(camera_id, frame)
                    if cv2.waitKey(interval) & 0xFF == ord('q'): break
                if proc.on_captured(camera, frame) == False:
                    break
        finally:
            proc.on_capture_stopped(camera)
            vcap.release()
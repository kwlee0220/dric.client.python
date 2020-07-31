import logging
import dric
import cv2

fps = 10
output_file = 'C:/temp/video.avi'

dric.set_log_level(logging.DEBUG)
platform = dric.connect()

class VideoCreater(dric.ImageProcessor):
    def __init__(self, output_file, fps):
        self.output_file = output_file
        self.fps = fps

    def on_capture_started(self, camera):
        self.writer = cv2.VideoWriter(self.output_file, cv2.VideoWriter_fourcc(*"DIVX"),
                                        self.fps, camera.resolution)

    def on_captured(self, camera, frame):
        self.writer.write(frame)

    def on_capture_stopped(self, camera):
        self.writer.release()

dric.Camera.capture('cam_00', fps, VideoCreater('C:/temp/video.avi', fps), True)
dric.disconnect()
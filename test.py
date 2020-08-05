import logging
import dric
import dric.utils
import cv2
from dric.dric_types import CameraFrame

dric.set_log_level(logging.DEBUG)
dric.connect()

camera_frames = dric.get_topic("dric/camera_frames")
# bbox_tracks = dric.get_topic("dric/bbox_tracks")

def on_camera_frame(bytes):
    try:
        rec = CameraFrame.SCHEMA.load_record_from_bytes(bytes)
        mat = dric.utils.from_bstring_to_mat(rec['image'])
        cv2.imshow(rec['camera_id'], mat)
        cv2.waitKey(10)
    except Exception as e:
        print(e)

camera_frames.subscribe(on_camera_frame)
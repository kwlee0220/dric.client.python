import logging
import dric
import dric.utils
import cv2

dric.set_log_level(logging.DEBUG)
dric.connect()

camera_frames = dric.get_topic("dric/camera_frames")
# bbox_tracks = dric.get_topic("dric/bbox_tracks")

def on_camera_frame(frame):
    try:
        mat = dric.utils.from_bstring_to_mat(frame.image)
        cv2.imshow(frame.camera_id, mat)
        cv2.waitKey(10)
    except Exception as e:
        print(e)

camera_frames.subscribe(on_camera_frame)
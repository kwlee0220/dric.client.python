import logging
import dric
import dric.utils
import cv2

dric.set_log_level(logging.DEBUG)
dric.connect()

ds = dric.get_dataset("topics/dric/camera_frames")
for record in ds.read():
    mat = dric.utils.from_bstring_to_mat(record.image)
    cv2.imshow(record.camera_id, mat)
    cv2.waitKey(10)
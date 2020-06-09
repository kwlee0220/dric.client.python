import dric
import dric.utils
import cv2

dric.connect()
camera_frames = dric.get_topic("dric/camera_frames")
bbox_tracks = dric.get_topic("dric/bbox_tracks")

def on_camera_frame(frame):
    mat = dric.utils.from_bstring_to_mat(frame.image)
    cv2.imshow("mat", mat)
    cv2.waitKey(10)
 #   track = dric.ObjectBBoxTrack(frame.camera_id, "obj_01", None, 0, frame.ts)
 #   bbox_tracks.publish(track)

camera_frames.subscribe(on_camera_frame)
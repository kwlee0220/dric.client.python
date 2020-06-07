
from dric.client import DrICClient
from dric.types import *

dric = DrICClient.connect("localhost", 10703)

camera_frames = dric.get_topic(CameraFrame, "dric/camera_frames")
bbox_tracks = dric.get_topic(ObjectBBoxTrack, "dric/bbox_tracks")

def on_camera_frame(frame):
    print(frame.camera_id)
    track = ObjectBBoxTrack(frame.camera_id, "obj_01", None, 0, frame.ts)
    bbox_tracks.publish(track)

camera_frames.subscribe(on_camera_frame)
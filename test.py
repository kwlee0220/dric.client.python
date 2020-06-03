import dric.dric_client as dric
from dric.types import *

dric.open_client('dric_client.yaml')

camera_frames = dric.connect_topic(CameraFrame, "dric/camera_frames")
bbox_tracks = dric.connect_topic(ObjectBBoxTrack, "dric/bbox_tracks")

def on_camera_frame(frame):
    print(frame.camera_id)
    track = ObjectBBoxTrack(frame.camera_id, "obj_01", None, 0, frame.ts)
    bbox_tracks.publish(track)

camera_frames.subscribe(on_camera_frame, 1)
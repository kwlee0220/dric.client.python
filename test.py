import dric

client = dric.DrICClient.connect("localhost", 10703)

camera_frames = client.get_topic(dric.CameraFrame, "dric/camera_frames")
bbox_tracks = client.get_topic(dric.ObjectBBoxTrack, "dric/bbox_tracks")

def on_camera_frame(frame):
    print(frame.camera_id)
    track = dric.ObjectBBoxTrack(frame.camera_id, "obj_01", None, 0, frame.ts)
    bbox_tracks.publish(track)

camera_frames.subscribe(on_camera_frame)
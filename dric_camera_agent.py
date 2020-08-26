# import logging
import dric
import cv2

from dric.image_processor import ImageProcessor, ImageDisplay, RecordWriter, VideoCreater, run_image_process
class BBoxObjectTracker(ImageProcessor):
    def __init__(self, ds):
        self.schema = ds.record_schema

    def on_capture_started(self, ctx):
        pass

    def on_captured(self, ctx, ts):
        camera = ctx['camera']
        frame = ctx['frame']
        bstr = dric.to_bstring_from_mat(frame)
        ctx['record_list'] = dric.Record(self.schema, (camera.id, bstr, ts))

    def on_capture_stopped(self, ctx):
        pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('camera_id', help='camera id to capture')
    parser.add_argument('--output_dir', '-o', type=str, required=False, help='directory for created video files')
    parser.add_argument('--video_interval', '-i', type=str, default="1h", help='interval for a video in seconds')
    parser.add_argument('--fps', type=float, default=10.0, help='number of frames per second')
    parser.add_argument('--show', '-s', action='store_true', help='number of frames per second')
    parser.add_argument('--topic', '-t', type=str, default='dric/camera_frames', help='target topic name')
    args = parser.parse_args()

    def __open_camera():
        return dric.Camera(args.camera_id, args.fps)

    import logging
    logger = logging.getLogger("dric.camera_agent")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    dric.connect()
    try :
        camera = dric.Camera(args.camera_id, args.fps)
        topic = dric.get_dataset('topics/{0}'.format(args.topic))
        tracker = BBoxObjectTracker(topic)
        publisher = RecordWriter(topic)
        proc_list = [tracker, publisher]
        if args.output_dir:
            proc_list.append(VideoCreater(args.output_dir, args.video_interval))
        if args.show:
            proc_list.append(ImageDisplay())

        run_image_process(__open_camera, proc_list)
    finally:
        dric.disconnect()

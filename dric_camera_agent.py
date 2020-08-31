# import logging
import dric
import cv2

from dric.image_processor import ImageProcessor, ImageDisplay, RecordWriter, run_image_process
class BBoxObjectTracker(ImageProcessor):
    def __init__(self, camera_id, ds):
        self.camera_id = camera_id
        self.schema = ds.record_schema

    def on_capture_started(self, ctx, size):
        pass

    def on_captured(self, ctx, ts):
        frame = ctx['frame']
        bstr = dric.to_bstring_from_mat(frame)
        ctx['record_list'] = dric.Record(self.schema, (self.camera_id, bstr, ts))

    def on_capture_stopped(self, ctx):
        pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('camera_id', help='camera id to capture')
    parser.add_argument('--begin_time', '-b', type=str, help='the timestamp for the starting frame: YYYYMMDD:HHMMSS')
    parser.add_argument('--interval', "-i", type=str, default="5m", help='playback interval')
    parser.add_argument('--show', '-s', action='store_true', help='display the playback video stream')
    parser.add_argument('--topic', '-t', type=str, default='dric/camera_frames', help='target topic name')
    args = parser.parse_args()

    import logging
    logger = logging.getLogger("dric.camera_agent")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    dric.connect()
    try :
        topic = dric.get_dataset('topics/{0}'.format(args.topic))
        tracker = BBoxObjectTracker(args.camera_id, topic)
        publisher = RecordWriter(topic)
        proc_list = [tracker, publisher]
        if args.show:
            proc_list.append(ImageDisplay(args.camera_id))

        if args.begin_time is None:
            import datetime
            args.begin_time = dric.to_datetime_string(datetime.datetime.now())

        run_image_process(args.camera_id, proc_list, args.begin_time, args.interval)
    finally:
        dric.disconnect()

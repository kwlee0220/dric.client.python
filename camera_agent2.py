# import logging
import dric
import cv2

class BBoxObjectTracker:
    def __init__(self, ds, output_dir, interval):
        self.ds = ds
        self.output_dir = output_dir
        self.interval = interval

    def on_capture_started(self, camera):
        self.ds_writer = self.ds.open_writer()
        self.video_writer = None
        self.ds_writer.__enter__()

    def on_captured(self, camera, image, ts):
        if self.output_dir is not None:
            if not self.video_writer:
                self.video_writer = self.__open_video_writer(camera, ts)
            elif (ts - self.start_ts) >= self.interval:
                self.video_writer.release()
                self.video_writer = self.__open_video_writer(camera, ts)
            self.video_writer.write(image)

        bstr = dric.to_bstring_from_mat(image)
        rec = dric.Record(self.ds.record_schema, (camera.id, bstr, ts))
        self.ds_writer.write(rec)

    def on_capture_stopped(self, camera):
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None
        self.ds_writer.close()
        self.ds_writer.__exit__(None, None, None)

    def __open_video_writer(self, camera, ts):
        self.start_ts = ts

        from pathlib import Path
        video_dir_path = Path(self.output_dir)
        video_path = video_dir_path / '{0}_{1}.avi'.format(camera.id, int(self.start_ts))
        video_path.parent.mkdir(parents=True, exist_ok=True)
        return cv2.VideoWriter(str(video_path), cv2.VideoWriter_fourcc(*"DIVX"), camera.fps, camera.size)

def run(capture_fact, tracker, loop, show_image):
    try:
        capturer = capture_fact()
        tracker.on_capture_started(capturer)

        while ( 1 ):
            sleep_millis, frame = capturer.capture()
            if frame is not None:
                started = dric.current_millis()
                tracker.on_captured(capturer, frame, started)
                if show_image:
                    cv2.imshow(capturer.id, frame)
    
                elapsed = dric.current_millis() - started
                sleep_millis = max(sleep_millis - elapsed - 3, 1)
                if cv2.waitKey(sleep_millis) & 0xFF == ord('q'): break
            elif loop:
                capturer.release()
                capturer = capture_fact()
            else: break
    finally:
        tracker.on_capture_stopped(capturer)
        capturer.release()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('camera_id', help='camera id to capture')
    parser.add_argument('--output_dir', '-o', type=str, required=False, help='directory for created video files')
    parser.add_argument('--video_file', '-f', type=str, help='video file path')
    parser.add_argument('--video_interval', '-i', type=str, default="1h", help='interval for a video in seconds')
    parser.add_argument('--fps', type=float, default=10.0, help='number of frames per second')
    parser.add_argument('--loop', '-l', action='store_true', help='re-start to play at the end of the play')
    parser.add_argument('--show', '-s', action='store_true', help='number of frames per second')
    parser.add_argument('--topic', '-t', type=str, default='dric/camera_frames', help='target topic name')
    args = parser.parse_args()

    dric.connect()
    try :
        topic = dric.get_dataset('topics/{0}'.format(args.topic))
        tracker = BBoxObjectTracker(topic, args.output_dir, dric.parse_duration(args.video_interval))

        if args.video_file:
            def create_video_player():
                return dric.VideoPlayer(args.camera_id, args.video_file)
            capture_fact = create_video_player
        else:
            def create_video_player():
                return dric.get_camera(args.camera_id, args.fps)
            capture_fact = create_video_player

        run(capture_fact, tracker, args.loop, args.show)
    finally:
        dric.disconnect()

import logging
import cv2

__TEN_SECS = 10 * 1000

def run_image_process(camera_id, frame_proc_list, start_time, interval):
    from .utils import current_millis, parse_datetime_millis, millis_to_datetime, to_datetime_string, parse_duration
    started = parse_datetime_millis(start_time)
    interval_millis = parse_duration(interval)

    while True:
        lag = current_millis() - started
        while lag < interval_millis + __TEN_SECS:
            sleep_secs = max((interval_millis - lag) / 1000, 1)
            import time
            time.sleep(sleep_secs)
            lag = current_millis() - started
        start_time = to_datetime_string(millis_to_datetime(started))
        stop_time = to_datetime_string(millis_to_datetime(started + interval_millis))
        process_playback(camera_id, frame_proc_list, start_time, stop_time)
        started += interval_millis

def process_playback(camera_id, frame_proc_list, start_time, stop_time):
    from .camera import Playback
    play = Playback(camera_id, start_time, stop_time)
    play.start()
    try:
        ctx = {}
        frame, ts = play.capture()
        while frame:
            ctx['frame'] = frame
            for proc in frame_proc_list:
                proc.on_captured(ctx, ts)
            frame, ts = play.capture()
    finally:
        play.stop()


from abc import ABCMeta, abstractmethod
class ImageProcessor(metaclass=ABCMeta):
    logger = logging.getLogger("dric.img_proc")
    logger.setLevel(logging.INFO)

    @abstractmethod
    def on_capture_started(self, ctx, size): pass

    @abstractmethod
    def on_captured(self, ctx, ts): pass

    @abstractmethod
    def on_capture_stopped(self, ctx): pass


class ImageDisplay(ImageProcessor):
    def __init__(self, camera_id):
        self.show = True
        self.camera_id = camera_id

    def on_capture_started(self, ctx, size):
        import numpy as np
        self.empty_image = np.zeros((size.height, size.width, 3), np.uint8)
        cv2.putText(self.empty_image, 'monitoring {0}...'.format(self.camera_id), (30, int(size.height/2)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255,255,255), 2)

    def on_captured(self, ctx, ts):
        if self.show:
            cv2.imshow(self.camera_id, ctx['frame'])
        else:
            cv2.imshow(self.camera_id, self.empty_image)

    def on_capture_stopped(self, ctx):
        cv2.destroyWindow(self.camera_id)



class RecordWriter(ImageProcessor):
    def __init__(self, ds):
        self.ds = ds
        self.ds_writer = None

    def on_capture_started(self, ctx):
        self.ds_writer = self.ds.open_writer()
        self.ds_writer.__enter__()

    def on_captured(self, ctx, ts):
        record_list = ctx['record_list']
        if not isinstance(record_list, list):
            record_list = [record_list]
        for record in record_list:
            self.ds_writer.write(record)

    def on_capture_stopped(self, ctx):
        if self.ds_writer is not None:
            self.ds_writer.close()
            self.ds_writer.__exit__(None, None, None)


class VideoCreater(ImageProcessor):
    logger = logging.getLogger("dric.video.creater")

    def __init__(self, camera_id, output_dir, fps, video_interval):
        self.camera_id = camera_id
        self.output_dir = output_dir
        self.fps = fps
        self.video_interval_str = str(video_interval)
        from .utils import parse_duration
        self.video_interval = parse_duration(str(video_interval))
        self.video_file = None
        self.video_writer = None

    def on_capture_started(self, ctx, size):
        self.size = size

    def on_captured(self, ctx, ts):
        frame = ctx['frame']
        if self.video_writer is None:
            self.video_writer = self.__open_video_writer(ts)
        if (ts - self.start_ts) >= self.video_interval:
            self.video_writer.release()
            self.video_writer = self.__open_video_writer(ts)
        self.video_writer.write(frame)

    def on_capture_stopped(self, ctx):
        if self.video_writer is not None:
            self.video_writer.release()

    def __str__(self):
        if self.video_file:
            return 'VideoWriter: file=%s, fps=%f, interval=%s' % (self.video_file, self.fps, self.video_interval_str)
        else:
            return 'VideoWriter: file=unknown, fps=%s, interval=%s' % (self.fps, self.video_interval_str)

    def __open_video_writer(self, ts):
        self.start_ts = ts

        import time
        dt_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(ts / 1000.0))
        fname = '{0}_{1}.avi'.format(self.camera_id, dt_str)

        from pathlib import Path
        self.video_file = Path(self.output_dir) / fname
        self.video_file.parent.mkdir(parents=True, exist_ok=True)
        VideoCreater.logger.info('create a video file: {0}'.format(self.video_file))
        return cv2.VideoWriter(str(self.video_file), cv2.VideoWriter_fourcc(*"DIVX"), self.fps, self.size)
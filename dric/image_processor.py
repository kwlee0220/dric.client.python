import logging
import cv2

def run_image_process(camera, frame_proc_list):
    try:
        if type(frame_proc_list) != list:
            frame_proc_list = [frame_proc_list]
        display = next((proc for proc in frame_proc_list if isinstance(proc, ImageDisplay)), None)

        ctx = {'camera':camera}
        for proc in frame_proc_list:
            proc.on_capture_started(ctx)
        while ( 1 ):
            sleep_millis, frame = camera.capture()
            if frame is not None:
                from .utils import current_millis
                started = current_millis()
                ctx['frame'] = frame
                for proc in frame_proc_list:
                    proc.on_captured(ctx, started)

                elapsed = current_millis() - started
                sleep_millis = max(sleep_millis - elapsed - 3, 1)
                code = cv2.waitKey(sleep_millis) & 0xFF
                if code == ord('q'):
                    break
                elif code == ord('v') and display is not None:
                    display.show = not display.show
            else: break
    finally:
        for proc in frame_proc_list:
            proc.on_capture_stopped(ctx)
        camera.release()


from abc import ABCMeta, abstractmethod
class ImageProcessor(metaclass=ABCMeta):
    @abstractmethod
    def on_capture_started(self, ctx): pass

    @abstractmethod
    def on_captured(self, ctx, ts): pass

    @abstractmethod
    def on_capture_stopped(self, ctx): pass


class ImageDisplay(ImageProcessor):
    def __init__(self):
        self.show = True

    def on_capture_started(self, ctx):
        camera = ctx['camera']

        size = camera.size
        import numpy as np
        self.empty_image = np.zeros((size.height, size.width, 3), np.uint8)
        cv2.putText(self.empty_image, 'monitoring {0}...'.format(camera.id), (30, int(size.height/2)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255,255,255), 2)

    def on_captured(self, ctx, ts):
        camera = ctx['camera']
        if self.show:
            cv2.imshow(camera.id, ctx['frame'])
        else:
            cv2.imshow(camera.id, self.empty_image)

    def on_capture_stopped(self, ctx):
        cv2.destroyWindow(ctx['camera'].id)



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

    def __init__(self, output_dir, interval):
        self.output_dir = output_dir
        from .utils import parse_duration
        self.interval = parse_duration(str(interval))
        self.video_writer = None

    def on_capture_started(self, ctx):
        pass

    def on_captured(self, ctx, ts):
        camera = ctx['camera']
        frame = ctx['frame']
        if self.video_writer is None:
            self.video_writer = self.__open_video_writer(camera, ts)
        if (ts - self.start_ts) >= self.interval:
            self.video_writer.release()
            self.video_writer = self.__open_video_writer(camera, ts)
        self.video_writer.write(frame)

    def on_capture_stopped(self, ctx):
        if self.video_writer is not None:
            self.video_writer.release()

    def __open_video_writer(self, camera, ts):
        self.start_ts = ts

        import time
        dt_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(ts / 1000.0))
        fname = '{0}_{1}.avi'.format(camera.id, dt_str)

        from pathlib import Path
        video_path = Path(self.output_dir) / fname
        video_path.parent.mkdir(parents=True, exist_ok=True)
        VideoCreater.logger.info('create a video file: {0}'.format(video_path))
        return cv2.VideoWriter(str(video_path), cv2.VideoWriter_fourcc(*"DIVX"), 30, camera.size)
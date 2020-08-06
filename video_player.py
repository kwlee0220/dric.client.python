import logging
import dric
import cv2       
import time

class VideoPlayer:
    logger = logging.getLogger("dric.video")

    def __init__(self, id, file):
        self.id = id
        self.file = file
        self.vcap = cv2.VideoCapture(file)
        self.pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
        self.ts = time.time()

    def release(self):
        self.vcap.release()

    def read(self):
        ret, frame = self.vcap.read()
        if ret:
            pos = self.vcap.get(cv2.CAP_PROP_POS_MSEC)
            ts = time.time()
            idle_ts = int((pos - self.pos) - (ts - self.ts) - 10)
            self.pos = pos
            self.ts = ts
            if idle_ts > 5:
                if cv2.waitKey(idle_ts) & 0xFF == ord('q'):
                    return None
            return frame
        else:
            return None

    def __str__(self):
        return '{0}[{1}]'.format(type(self).__name__, self.id)

    @classmethod
    def play(cls, id, file, proc, show_image=False):
        player = VideoPlayer(id, file)
        try:
            cls.logger.info('start reading a video file=%s' % file)
            proc.on_capture_started(player)
            while ( 1 ):
                frame = player.read()
                if frame is None: break

                import time
                ts = int(round(time.time() * 1000))
                if cls.logger.isEnabledFor(logging.DEBUG):
                    cls.logger.info('capture a frame from {0}, ts={1}'.format(player, ts))

                if show_image:
                    cv2.imshow(id, frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'): break
                if proc.on_captured(player, frame, ts) == False:
                    cls.logger.info('client stopped capturing: player=' + player)
                    break
        finally:
            proc.on_capture_stopped(player)
            player.release()


class BBoxObjectTracker:
    def __init__(self, schema):
        self.schema = schema

    def on_capture_started(self, player):
        self.writer = topic.open_writer()
        self.writer.__enter__()

    def on_captured(self, player, image, ts):
        bstr = dric.to_bstring_from_mat(image)
        rec = dric.Record(self.schema, (player.id, bstr, ts))
        self.writer.write(rec)

    def on_capture_stopped(self, player):
        self.writer.__exit__(None, None, None)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('camera_id', help='camera id to capture')
    parser.add_argument('video_file', help='target video file path')
    parser.add_argument('--loop', '-l', action='store_true', help='re-start to play at the end of the play')
    parser.add_argument('--show', '-s', action='store_true', help='number of frames per second')
    parser.add_argument('--topic', '-t', type=str, default='dric/camera_frames', help='target topic name')
    args = parser.parse_args()

    dric.connect()

    topic = dric.get_dataset("/topics/" + args.topic)
    dric.set_log_level(logging.DEBUG)
    track = BBoxObjectTracker(topic.record_schema)
    VideoPlayer.play(args.camera_id, args.video_file, track, args.show)

    dric.disconnect()
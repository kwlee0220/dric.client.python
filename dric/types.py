
import dric_pb2

class ImageCoordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_proto(self, proto):
        return ImageCoordinate(proto.x, proto.y)
    def to_proto(self):
        return dric_pb2.ImageCoordinateProto(x=self.x, y=self.y)

class BoundingBox:
    def __init__(self, tl, br):
        self.tl = tl
        self.br = br

    @classmethod
    def from_proto(self, proto):
        return BoundingBox(proto.tl, proto.br)
    def to_proto(self):
        return dric_pb2.BoundingBoxProto(tl=self.tl, br=self.br)

class CameraFrame:
    def __init__(self, camera_id, image, ts):
        self.camera_id = camera_id
        self.image = image
        self.ts = ts

    @classmethod
    def from_proto(self, proto):
        return CameraFrame(proto.camera_id, proto.image, proto.ts)
    def to_proto(self):
        return dric_pb2.CameraFrameProto(camera_id=self.camera_id, image=self.image, ts=self.ts)

    @classmethod
    def from_bytes(self, bytes):
        proto = dric_pb2.CameraFrameProto()
        proto.ParseFromString(bytes)
        return CameraFrame.from_proto(proto)
    def to_bytes(self):
        return self.to_proto().SerializeToString()

class ObjectBBoxTrack:
    def __init__(self, camera_id, luid, bbox, heading, ts):
        self.camera_id = camera_id
        self.luid = luid
        self.bbox = bbox
        self.heading = heading
        self.ts = ts

    @classmethod
    def from_proto(self, proto):
        return ObjectBBoxTrack(proto.camera_id, proto.luid, proto.bbox, proto.heading, proto.ts)
    def to_proto(self):
        return dric_pb2.ObjectBBoxTrackProto(camera_id=self.camera_id, luid=self.luid, bbox=self.bbox,
                                            heading=self.heading, ts=self.ts)

    @classmethod
    def from_bytes(self, bytes):
        proto = dric_pb2.ObjectBBoxTrackProto()
        proto.ParseFromString(bytes)
        return ObjectBBoxTrack.from_proto(proto)
    def to_bytes(self):
        return self.to_proto().SerializeToString()

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_proto(self, proto):
        return Coordinate(proto.x, proto.y)
    def to_proto(self):
        return dric_pb2.CoordinateProto(x=self.x, y=self.y)

class ObjectTrack:
    def __init__(self, camera_id, luid, lonlat, azimuth, ts):
        self.camera_id = camera_id
        self.luid = luid
        self.lonlat = lonlat
        self.azimuth = azimuth
        self.ts = ts

    @classmethod
    def from_proto(self, proto):
        return ObjectTrack(proto.camera_id, proto.luid, proto.lonlat, proto.azimuth, proto.ts)
    def to_proto(self):
        return dric_pb2.ObjectTrackProto(camera_id=self.camera_id, luid=self.luid, lonlat=self.lonlat,
                                            azimuth=self.azimuth, ts=self.ts)

    @classmethod
    def from_bytes(self, bytes):
        proto = dric_pb2.ObjectTrackProto()
        proto.ParseFromString(bytes)
        return ObjectTrack.from_proto(proto)
    def to_bytes(self):
        return self.to_proto().SerializeToString()
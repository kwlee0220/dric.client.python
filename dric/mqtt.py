
# import paho.mqtt.client as mqtt
# from .client import platform
# from .dric_types import CameraFrame, ObjectBBoxTrack
# __builtin_topic_infos = {"dric/camera_frames": CameraFrame,
#                         "dric/bbox_tracks": ObjectBBoxTrack }

class TopicNotFound(Exception):
    def __init__(self, name):
        self.topic_name = name

# def get_topic(topic, msg_handler=None):
#     if not msg_handler:
#         msg_handler = __builtin_topic_infos[topic]
#         if not msg_handler:
#             raise TopicNotFound(topic)
#     topic_client = mqtt.Client()
#     topic_server = platform().get_service_end_point('topic_server')
#     topic_client.connect(topic_server.host, topic_server.port)
#     return MqttTopic(topic_client, topic, msg_handler)

class MqttTopic:
    def __init__(self, client, topic, msg_handler=None):
        self.mqtt_client = client
        self.topic = topic
        self.msg_handler = msg_handler

    def publish(self, msg, qos=0, retain=False):
        self.mqtt_client.publish(self.topic, msg.to_bytes(), qos, retain)
        
    def subscribe(self, on_message, qos=0):
        self.on_message = on_message
        self.mqtt_client.on_message = self.__on_message
        self.mqtt_client.subscribe(self.topic, qos)
        self.mqtt_client.loop_forever()
        
    def subscribe_async(self, on_message, qos=0):
        self.on_message = on_message
        self.mqtt_client.on_message = self.__on_message
        self.mqtt_client.subscribe(self.topic, qos)
        self.mqtt_client.loop_start()

    def unsubscribe(self):
        self.mqtt_client.loop_stop
        self.mqtt_client.unsubscribe(self.topic)

    def __on_message(self, client, data, msg):
        if self.msg_handler:
            self.on_message(self.msg_handler.from_bytes(msg.payload))
        else:
            self.on_message(msg.payload)

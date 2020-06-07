import dric_pb2
from .types import *

class MqttTopic:
    def __init__(self, client, msg_type, topic):
        self.mqtt_client = client
        self.msg_type = msg_type
        self.topic = topic

    def publish(self, msg, qos=0, retain=False):
        self.mqtt_client.publish(self.topic, msg.to_bytes(), qos, retain)
        
    def subscribe(self, on_message, qos=0):
        self.on_message = on_message
        self.mqtt_client.on_message = self.__on_message
        self.mqtt_client.subscribe(self.topic, qos)
        self.mqtt_client.loop_forever()

    def unsubscribe(self):
        self.mqtt_client.loop_stop
        self.mqtt_client.unsubscribe(self.topic)

    def __on_message(self, client, data, msg):
        self.on_message(self.msg_type.from_bytes(msg.payload))
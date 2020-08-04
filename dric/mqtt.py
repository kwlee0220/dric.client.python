
import paho.mqtt.client as mqtt

class MqttTopic:
    def __init__(self, broker_host, broker_port, topic_name, msg_handler=None):
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(broker_host, broker_port)
        self.topic_name = topic_name
        self.msg_handler = msg_handler

    def publish(self, msg, qos=0, retain=False):
        self.mqtt_client.publish(self.topic_name, msg.to_bytes(), qos, retain)
        
    def subscribe(self, on_message, qos=0):
        self.on_message = on_message
        self.mqtt_client.on_message = self.__on_message
        self.mqtt_client.subscribe(self.topic_name, qos)
        self.mqtt_client.loop_forever()
        
    def subscribe_async(self, on_message, qos=0):
        self.on_message = on_message
        self.mqtt_client.on_message = self.__on_message
        self.mqtt_client.subscribe(self.topic_name, qos)
        self.mqtt_client.loop_start()

    def unsubscribe(self):
        self.mqtt_client.loop_stop
        self.mqtt_client.unsubscribe(self.topic_name)

    def __on_message(self, client, data, msg):
        if self.msg_handler:
            self.on_message(self.msg_handler.from_bytes(msg.payload))
        else:
            self.on_message(msg.payload)

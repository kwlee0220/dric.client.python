import yaml
import paho.mqtt.client as mqtt
from .topics import MqttTopic

__dric_client = None

def open_client(conf_file):
    global __dric_client
    __dric_client = DricClient(conf_file)

def connect_topic(msg_type, topic):
    return MqttTopic(__dric_client, msg_type, topic)
    
class DricClient:
    def __init__(self, conf_file):
        with open(conf_file) as file:
            self.conf = yaml.load(file, Loader=yaml.FullLoader)

    def connect_mqtt(self):
        client = mqtt.Client()
        mqtt_conf = self.conf["mqtt"]
        client.connect(mqtt_conf["host"], int(mqtt_conf["port"]))
        return client

if __name__ == '__main__':
    pass
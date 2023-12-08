import random
import paho.mqtt.client as mqtt

class Sensor:
    def __init__(self, id, url, port):
        self.id = id
        self.client = mqtt.Client()
        self.client.connect(url, port)
        self.client.on_connect = self.on_connect

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")


class Temperature_sensor(Sensor):
    def __init__(self, id, url, port):
        super().__init__(id, url, port)
    
    def __get_temperature(self):
        return float(random.randrange(0, 300)) / 10

    def send_data(self):
        self.client.loop_start()
        self.client.publish("data/temperature", self.__get_temperature(), 1)
        self.client.loop_stop()


class Humidity_sensor(Sensor):
    def __init__(self, id, url, port):
        super().__init__(id, url, port)
        
    def __get_humidity(self):
        return random.randrange(30, 100)
    
    def send_data(self):
        self.client.loop_start()
        self.client.publish("data/humidity", self.__get_humidity(), 1)
        self.client.loop_stop()
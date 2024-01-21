import random
import paho.mqtt.client as mqtt
import math


class MQTT_item:
    sleutel_transpositie = 3
    sleutel_caesar = 9
    alfabet = "abcdefghijklmnopqrstuvw1234567890"

    def __init__(self, id, url, port):
        self.id = id
        self.client = mqtt.Client()
        self.client.connect(url, port)
        self.client.on_connect = self.__on_connect

    def __on_connect(self, client, userdata, flags, rc):
        print(f"{self.id}: connected with result code {rc}")

    def __encrypt_data(self, data):
        msg_len = float(len(data.lower()))
        msg_lst = list(data)

        row = int(math.ceil(msg_len / self.sleutel_transpositie))

        fill_null = int((row * self.sleutel_transpositie) - msg_len)
        msg_lst.extend('_' * fill_null)

        matrix = [msg_lst[i: i + self.sleutel_transpositie]
                  for i in range(0, len(msg_lst), self.sleutel_transpositie)]

        encrypted_data_transpositie = ''
        for _ in range(self.sleutel_transpositie):
            encrypted_data_transpositie += ''.join([row[_]
                                                    for row in matrix])

        encrypted_data_caesar = ""
        for let in encrypted_data_transpositie:
            encrypted_data_caesar += self.alfabet[(
                self.alfabet.find(let) + self.sleutel_caesar) % len(self.alfabet)]
        return encrypted_data_caesar

    def decrypt_data(self, encrypted_data):
        caesar_decrypted_data = ""
        for let in encrypted_data:
            caesar_decrypted_data += self.alfabet[(self.alfabet.find( let) - self.sleutel_caesar) % len(self.alfabet)]

        numOfColumns = math.ceil(len(caesar_decrypted_data) / self.sleutel_transpositie)
        numOfRows = self.sleutel_transpositie

        numOfShadedBoxes = (numOfColumns * numOfRows) - len(caesar_decrypted_data)
        plaintext = [''] * numOfColumns
        col = 0
        row = 0
        for symbol in caesar_decrypted_data:
            plaintext[col] += symbol
            col += 1
            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1
                
        return ''.join(plaintext).replace("_", "").replace("0", "")

    def publish_data(self, topic, data):
        self.client.loop_start()
        self.client.publish(f"data/{topic}", data, 1)
        self.client.loop_stop()

    def publish_data_encrypted(self, topic, data):
        self.client.loop_start()
        self.client.publish(f"data/{topic}/encrypted", self.__encrypt_data(str(data)), 1)
        self.client.loop_stop()


class Temperature_sensor(MQTT_item):
    topic = "temperature"
    
    def __init__(self, id, url, port):
        super().__init__(id, url, port)

    def __get_temperature(self):
        return float(random.randrange(0, 301)) / 10

    def send_data(self):
        self.publish_data(self.topic, self.__get_temperature())

    def send_data_encrypted(self):
        self.publish_data_encrypted(self.topic, self.__get_temperature())


class Humidity_sensor(MQTT_item):
    topic = "humidity"
    
    def __init__(self, id, url, port):
        super().__init__(id, url, port)

    def __get_humidity(self):
        return random.randrange(30, 101)

    def send_data(self):
        self.publish_data(self.topic, self.__get_humidity())

    def send_data_encrypted(self):
        self.publish_data_encrypted(self.topic, self.__get_humidity())


class Security_panel(MQTT_item):
    topic = "security"
    
    def __init__(self, id, url, port):
        super().__init__(id, url, port)

    def __security(self):
        _ = random.randrange(0, 2)

        if _ == 0:
            return "lock"
        elif _ == 1:
            return "unlock"

    def send_data(self):
        self.publish_data(self.topic, self.__security())

    def send_data_encrypted(self):
        self.publish_data_encrypted(self.topic, self.__security())


class Door_lock(MQTT_item):
    topic = "security"
    
    def __init__(self, id, url, port):
        super().__init__(id, url, port)
        self.client.subscribe(f"data/{self.topic}/#", qos=1)
        self.client.on_message = self.__on_message
        self.__connect()

    def __connect(self):
        self.client.loop_start()

    def __on_message(self, client, userdata, msg):
        data = str(msg.payload)[2:-1]
        popup = ""
        if msg.topic == "data/security/encrypted":
            data = self.decrypt_data(data)
        else:
            popup += "!! Insecure !! "

        if data == "unlock":
            popup += "Unlocking door"
        elif data == "lock":
            popup += "Locking door"
        else:
            popup = "Error"
        
        print(popup)

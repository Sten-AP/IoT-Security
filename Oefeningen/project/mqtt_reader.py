import paho.mqtt.client as mqtt

url = "localhost"
port = 1000

client = mqtt.Client()
client.connect(url, port)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("data/#", qos=1)


def on_message(client, userdata, msg):
    data = str(msg.payload)[2:-1]
    print(f"{msg.topic}: {data}")


client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

import paho.mqtt.client as mqtt

url = "localhost"
port = 1000

client = mqtt.Client()
client.connect(url, port)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("data/#", qos=1)

def on_message(client, userdata, msg):
    data = msg.payload
    if msg.topic == "data/temperature":
        data = float(msg.payload)
    elif msg.topic == "data/humidity":
        data = int(msg.payload)
        
    print(f"{msg.topic}: {data}")

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
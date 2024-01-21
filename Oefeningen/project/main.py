from classes import Temperature_sensor, Humidity_sensor, Security_panel, Door_lock
from time import sleep

url = "localhost"
port = 1000

temperature_sensor = Temperature_sensor("id-temp-1", url, port)
humidity_sensor = Humidity_sensor("id-hum-1", url, port)
security_panel = Security_panel("id-security-1", url, port)
door_lock = Door_lock("id-lock-1", url, port)

while True:
    # temperature_sensor.send_data()
    temperature_sensor.send_data_encrypted()
    sleep(2)

    # humidity_sensor.send_data()
    humidity_sensor.send_data_encrypted()
    sleep(2)

    # security_panel.send_data()
    security_panel.send_data_encrypted()
    sleep(10)

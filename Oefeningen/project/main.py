from classes import Temperature_sensor, Humidity_sensor

url = "localhost"
port = 1000

temperature_sensor = Temperature_sensor("id-temp-1", url, port)
temperature_sensor.send_data()

humidity_sensor = Humidity_sensor("id-hum-1", url, port)
humidity_sensor.send_data()
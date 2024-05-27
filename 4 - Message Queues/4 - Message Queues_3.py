# 3.  Implement a Python program that publishes messages to the topic "/example/1" every 0.5 seconds. 
# The program publishes integer numbers starting from 1 and raising the value by 1 on every publish. 
# That is, it publishes integers in order starting from 1.
# Check with mosquitto_sub that the messages are really being published onto the topic.
# *Install paho-mqtt-python:
# pip install paho-mqtt

import paho.mqtt.client as mqtt
import time

broker = "localhost"

def cb_on_publish(client, userdata, result):
    print("Data published.")

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
mqtt_client.on_publish = cb_on_publish
#mqtt_client.username_pw_set(username = "your_username", password = "your_password")
print("Connecting...")
mqtt_client.connect(broker)

num = 1

try:
    print("Press CTRL+C to exit...")
    while True:
        mqtt_client.publish("/example/1", num)
        num += 1
        time.sleep(0.5)
except KeyboardInterrupt:
    mqtt_client.disconnect()
    print("\nClient disconnected.")
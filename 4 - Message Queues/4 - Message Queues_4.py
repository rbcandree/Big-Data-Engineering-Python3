# 4.  Implement a Python program that subscribes to "/example/1". 
# On every message that the program sees on that channel, it multiplies the integer value by 2 and publishes the result 
# on "/example/2". 
# Check with mosquitto_sub that the messages are really being published onto the topic.

import paho.mqtt.client as mqtt
from queue import Queue

broker = "localhost"

# thread-safe queue for the messages
q = Queue()

def main_loop():
    mqtt_client.loop_start()
    #mqtt_client.username_pw_set(username = "your_username", password = "your_password")
    mqtt_client.subscribe("/example/1", 1)
    try:
        print("Press CTRL+C to exit...")
        while True:
            message = q.get()
            if message is None:
                continue
            #decoded_message = str(message.payload.decode("utf-8"))
            decoded_message = message.payload.decode("utf-8")
            print(decoded_message)
            mqtt_client.publish("/example/2", int(decoded_message)*2)
    except KeyboardInterrupt:
        mqtt_client.disconnect()
        print("\nClient disconnected.")

# our callback functions
def cb_on_message(client, userdata, message):
    q.put(message)

def cb_on_disconnect(client, userdata):
    mqtt_client.loop_stop()

def cb_on_publish(client, userdata, result):
    print("Data published.")

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, clean_session = True)
# define which function to use as callback when we receive messages
mqtt_client.on_message = cb_on_message
mqtt_client.on_disconnect = cb_on_disconnect
mqtt_client.connect(broker)
main_loop()
#mqtt_client.loop_forever() - as an alternative to main_loop()
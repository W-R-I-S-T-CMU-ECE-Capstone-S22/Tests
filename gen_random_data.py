import time, string
import random
import paho.mqtt.client as mqtt

TOPIC = "wrist/data/sensors"

letters = string.ascii_letters


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # client.subscribe(TOPIC)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))

    client.loop_stop()

# def on_message(client, userdata, msg):
#     print(list(msg.payload))

client = mqtt.Client("client" + str(random.randrange(100000, 999999)), clean_session=True)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
# client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_start()

while (1):
    time.sleep(0.05)
    client.publish(TOPIC, ''.join(random.choice(letters) for i in range(3)))

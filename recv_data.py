import time
import random
import paho.mqtt.client as mqtt

TOPIC = "wrist/data/sensors"

NUM_SENSORS = 10
OUT_FILE_NAME = "data.txt"

out_file = open(OUT_FILE_NAME, "w")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(TOPIC)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))

    client.loop_stop()

def on_message(client, userdata, msg):
    data = list(msg.payload)

    timestamp = int.from_bytes(bytes(data[:-NUM_SENSORS]), "little")
    curr_time = time.time()
    elapsed = curr_time - timestamp

    sensor_data = data[-NUM_SENSORS:]
    print(elapsed, ":\t", sensor_data)

    out_file.write(f"{curr_time}, {sensor_data}\n")

client = mqtt.Client("client" + str(random.randrange(100000, 999999)), clean_session=True)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_start()

while (1):
    try:
        pass
    except KeyboardInterrupt:
        out_file.close()
        break

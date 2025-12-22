import time
import json
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import datetime

# =========================
# SENSOR SETUP
# =========================
dht = adafruit_dht.DHT11(board.D4)  # GPIO4

# =========================
# MQTT CONFIGURATION
# =========================
BROKER = "localhost"
PORT = 1883
TOPIC = "raspi5/sensor/dht11"

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT, 60)

# =========================
# MAIN LOOP
# =========================
while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity

        if temperature is not None and humidity is not None:
            payload = {
                "temperature": temperature,
                "humidity": humidity,
                "time": datetime.datetime.now().isoformat()
            }

            client.publish(TOPIC, json.dumps(payload))
            print("Published:", payload)

    except RuntimeError:
        pass

    time.sleep(3)

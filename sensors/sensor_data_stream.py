import requests
import time
import random
from datetime import datetime

WELLS = ["W-101","W-102","W-103","W-104","W-105"]

state = {
    "pressure": 70,
    "temperature": 40,
    "flow_rate": 200,
    "vibration": 1.0,
    "tank_level": 80
}

sensor_intervals = {
    "pressure": 1,
    "temperature": 2,
    "flow_rate": 1,
    "vibration": 0.2,
    "tank_level": 30
}

last_emit = {k: 0 for k in sensor_intervals}
buffer = []

def drift(value, change):
    return value + random.uniform(-change, change)

def maybe_anomaly(sensor, value):
    if random.random() < 0.01:
        return value * random.uniform(1.5, 2)
    return value


EDGE_URL = "http://edge_microservice:5001/sensor"

while True:
    try:
        requests.post(EDGE_URL, json={"test":1})
        print("Edge microservice'e bağlandı!")
        break
    except requests.exceptions.ConnectionError:
        print("Edge microservice hazır değil, 5 sn bekleniyor...")
        time.sleep(5)

while True:
    now = time.time()
    well_id = random.choice(WELLS)

    for sensor, interval in sensor_intervals.items():

        if now - last_emit[sensor] >= interval:

            if sensor == "pressure":
                state[sensor] = drift(state[sensor],0.3)
            elif sensor == "temperature":
                state[sensor] = drift(state[sensor],0.2)
            elif sensor == "flow_rate":
                state[sensor] = drift(state[sensor],2)
            elif sensor == "vibration":
                state[sensor] = drift(state[sensor],0.1)
            elif sensor == "tank_level":
                state[sensor] = drift(state[sensor],0.05)

            value = maybe_anomaly(sensor,state[sensor])

            event = {
                "timestamp": datetime.utcnow().isoformat(),
                "well_id": well_id,
                "sensor": sensor,
                "value": round(value,2)
            }

            buffer.append(event)

            last_emit[sensor] = now

    # gateway batch send (5–15 event)
    if len(buffer) >= random.randint(5,15):

        # out-of-order simulation
        random.shuffle(buffer)

        for e in buffer:
            requests.post(EDGE_URL, json=e)

        buffer = []

    # jitter
    time.sleep(random.uniform(0.05,0.2))


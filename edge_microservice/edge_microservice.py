import time
from flask import Flask, request
from kafka import KafkaProducer
import json
import os

app = Flask(__name__)

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "host.docker.internal:9092")

# Retry logic ile producer
producer = None
while producer is None:
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        print("Kafka'ya bağlandı!")
    except Exception as e:
        print(f"Kafka hazır değil: {e}, 5 sn bekleniyor...")
        time.sleep(5)

@app.route("/sensor", methods=["POST"])
def sensor():
    data = request.json
    print(f"Edge microservice'e gelen veri: {data}")
    producer.send("sensor_data", data)
    producer.flush()
    return {"status":"ok"}

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5001)
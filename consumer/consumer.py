import time
import json
import os
from kafka import KafkaConsumer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

consumer = None
while consumer is None:
    try:
        consumer = KafkaConsumer(
            "sensor_data",  # topic adını buraya göre değiştir
            bootstrap_servers=KAFKA_BROKER,
            auto_offset_reset="earliest",
            group_id="sensor-consumer",
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )
        print("Kafka'ya bağlandı!")
    except Exception as e:
        print(f"Kafka hazır değil: {e}, 5 sn bekleniyor...")
        time.sleep(5)

print("Consumer başladı...")

for message in consumer:
    print(message.value)
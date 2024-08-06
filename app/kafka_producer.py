from confluent_kafka import Producer
import json
import time

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka server address
    'client.id': 'python-producer'
}

# Create Kafka producer instance
producer = Producer(conf)

# Function to deliver message
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Sample data to send
data = [
    {"id": "1", "name": "Alice", "timestamp": "2024-08-05T12:00:00Z"},
    {"id": "2", "name": "Bob", "timestamp": "2024-08-05T12:01:00Z"}
]

# Send data to Kafka
for record in data:
    producer.produce('events', key=record['id'], value=json.dumps(record), callback=delivery_report)
    producer.flush()
    time.sleep(1)

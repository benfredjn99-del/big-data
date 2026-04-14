from kafka import KafkaConsumer
import json

# Configuration
TOPIC_NAME = 'hospital-alerts'
KAFKA_SERVER = 'kafka:29092'

print(f"--- Starting Consumer for topic: {TOPIC_NAME} ---")

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=[KAFKA_SERVER],
    auto_offset_reset='earliest',  # Start from the beginning of the topic
    enable_auto_commit=True,
    group_id='hospital-monitoring-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    api_version=(0, 10)
)

try:
    for message in consumer:
        event = message.value
        # Distinct formatting for Alerts vs Normal events
        if event.get('EventType') == 'ALERT':
            print(f"🚨 ALERT: Patient {event.get('PatientID')} (Age: {event.get('Age')}) requires attention!")
        else:
            print(f"✅ NORMAL: Patient {event.get('PatientID')} processed.")
            
except KeyboardInterrupt:
    print("\nStopping consumer...")
finally:
    consumer.close()
from kafka import KafkaProducer
import json
import time

# Add it here as a parameter
producer = KafkaProducer(
    bootstrap_servers='kafka:29092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    api_version=(0, 10)
)

# Read events.json
try:
    with open('/data/events.json') as f:
        for line in f:
            # Skip empty lines if any
            if not line.strip():
                continue
                
            event = json.loads(line)
            event['EventType'] = 'ALERT' if event['Age'] > 70 else 'NORMAL'
            
            print(f"Sending: {event}") # Useful for debugging
            producer.send('hospital-alerts', event)
            producer.flush()
            time.sleep(2) 
            
            
except FileNotFoundError:
    print("Error: /data/events.json not found. Check your volume mapping!")
except Exception as e:
    print(f"An error occurred: {e}")
import json
import time

from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_detail"
ORDER_LIMIT = 8

producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("\n Generating one unique order every 5 seconds! \n")

for i in range(ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"cust{i}",
        "total_cost": i,
        "items": "burger,sandwich",
    }

    producer.send("order_details", json.dumps(data).encode("utf-8"))
    print(f"Order#{i+1} Complete")
    time.sleep(5)

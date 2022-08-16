import json

from kafka import KafkaConsumer


ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"


consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)

emails_sent_so_far = set()
print("\n Email Sender now started! \n")
while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["customer_email"]
        emails_sent_so_far.add(customer_email)
        print(f"Email sent: {customer_email}  - count: {len(emails_sent_so_far)}")

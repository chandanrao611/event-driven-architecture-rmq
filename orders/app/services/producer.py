import json
import pika
from app.config.rabbitmq import get_rabbitmq_connection

EXCHANGE_NAME = "orders_exchange"

def publish_event(event_name: str, payload: dict):
    connection = None
    try:
        connection = get_rabbitmq_connection()

        channel = connection.channel()

        channel.exchange_declare(
            exchange=EXCHANGE_NAME,
            exchange_type="fanout",
            durable=True
        )

        message = {
            "event": event_name,
            "data": payload
        }
        #Durable Queue + Persistent Messages
        # properties
        for i in range(1000000):
            channel.basic_publish(
                exchange=EXCHANGE_NAME,
                routing_key="",
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2
                )
            )

        print(f"✅ Published event: {event_name}")

    except Exception as e:
        print(f"❌ Publish failed: {e}")

    finally:
        if connection and connection.is_open:
            print(f"✅ Published connection.is_open: {connection.is_open}")
            connection.close()
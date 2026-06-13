import json

from app.config.rabbitmq import get_rabbitmq_connection
from app.events.event_types import ORDER_CREATED

EXCHANGE_NAME = "orders_exchange"
QUEUE_NAME = "notification_queue"


def process_message(ch, method, properties, body):
    try:
        message = json.loads(body)

        event_name = message.get("event")
        data = message.get("data")

        print(f"\n📨 Received Event: {event_name}")
        print(f"📄 Payload: {data}")

        # Handle specific events
        if event_name == ORDER_CREATED:
            send_order_notification(data)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"Error processing message: {e}")


def send_order_notification(order_data):
    print(
        f"🔔 Notification: Order {order_data['id']} created successfully"
    )


def start_consumer():
    print("Connecting to RabbitMQ...")
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    print("Connected!")
    channel.exchange_declare(
        exchange=EXCHANGE_NAME,
        exchange_type="fanout",
        durable=True
    )

    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True
    )

    channel.queue_bind(
        exchange=EXCHANGE_NAME,
        queue=QUEUE_NAME
    )

    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=process_message
    )

    print("🚀 Notification Service Started")
    print("👂 Waiting for events...")

    channel.start_consuming()
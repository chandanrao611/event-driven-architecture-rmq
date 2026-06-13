import pika
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = "guest"
RABBITMQ_PASSWORD = "guest"

def get_rabbitmq_connection():
    credentials = pika.PlainCredentials(
        RABBITMQ_USERNAME,
        RABBITMQ_PASSWORD
    )

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=credentials
        )
    )

    return connection


def check_rabbitmq_connection():
    try:
        connection = get_rabbitmq_connection()

        if connection.is_open:
            print("✅ RabbitMQ connected successfully")

        connection.close()
        return True

    except Exception as e:
        print(f"❌ RabbitMQ connection failed: {e}")
        return False
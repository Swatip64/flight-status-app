# app/rabbitmq_service.py
import pika

# Define RabbitMQ server credentials
rabbitmq_host = 'localhost'
rabbitmq_port = 5672
rabbitmq_user = 'guest'
rabbitmq_password = 'guest'

# Establish a connection to RabbitMQ
connection_params = pika.ConnectionParameters(
    host=rabbitmq_host,
    port=rabbitmq_port,
    credentials=pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
)

# Create a connection and channel
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the notification queue
notification_queue = 'notification_queue'
channel.queue_declare(queue=notification_queue)

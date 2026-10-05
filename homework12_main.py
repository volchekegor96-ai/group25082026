import os
import ssl
import time
import urllib.parse
import pika
from dotenv import load_dotenv

load_dotenv()

amqp_url = f"amqps://{os.getenv('AMQP_USERNAME')}:{os.getenv('AMQP_PASSWORD')}@{os.getenv('AMQP_HOST')}:{os.getenv('AMQP_PORT', 5671)}/{os.getenv('AMQP_VIRTUAL_HOST')}"
url = urllib.parse.urlparse(amqp_url)

ssl_context = ssl.create_default_context()
connection_params = pika.ConnectionParameters(
    host=url.hostname,
    port=url.port,
    virtual_host=url.path[1:],
    credentials=pika.PlainCredentials(url.username, url.password),
    ssl_options=pika.SSLOptions(context=ssl_context)
)


def send_message():
    with pika.BlockingConnection(connection_params) as connection:
        channel = connection.channel()
        channel.queue_declare(queue='weather', durable=True)
        message = "Weather report for today. By Egor Volchek."
        channel.basic_publish(
            exchange='',
            routing_key='weather',
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )
        print(f"Sent: '{message}'")


def receive_messages():
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue='weather', durable=True)

    def callback(ch, method, properties, body):
        print(f"Received: {body.decode()}")
        time.sleep(2)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='weather', on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    send_message()
    try:
        receive_messages()
    except KeyboardInterrupt:
        pass

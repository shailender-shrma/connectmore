import pika
from django.conf import settings
params = pika.URLParameters(settings.RABBITMQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="hello")


def publish(data):
    global channel,connection
    if channel.is_closed or connection.is_closed:
        connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_URL))
        channel = connection.channel()
    import json
    channel.basic_publish(exchange="", routing_key="hello", body=json.dumps(data))
    
    print(data)
    
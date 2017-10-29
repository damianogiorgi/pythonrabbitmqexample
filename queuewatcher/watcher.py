#!/usr/bin/env python
import pika
import os
import time
import sys

server = os.environ.get('RABBITMQ_HOST')
queue = os.environ.get('RABBITMQ_QUEUE')

print("Sleeping for 10 seconds..")
time.sleep(6)


#channel.queue_declare(queue=queue, durable=True)


while True:
    server = os.environ.get('RABBITMQ_HOST')
    queue = os.environ.get('RABBITMQ_QUEUE')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=server))
    channel = connection.channel()
    queue = channel.queue_declare(queue=queue, passive=True)
    queue_size = queue.method.message_count
    print("Queue size: " + str(queue_size))
    sys.stdout.flush()

    connection.close()
    time.sleep(2)

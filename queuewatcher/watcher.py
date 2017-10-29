#!/usr/bin/env python
import pika
import os
import time
import sys

server = os.environ.get('RABBITMQ_HOST')
queue_info = str(os.environ.get('RABBITMQ_QUEUE'))

print("Sleeping for 6 seconds..")
time.sleep(6)


#channel.queue_declare(queue=queue, durable=True)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=server))
while True:

    channel = connection.channel()
    queue = channel.queue_declare(queue=queue_info, passive=True)
    queue_size = queue.method.message_count
    print("Queue size: " + str(queue_size))
    sys.stdout.flush()
    time.sleep(2)
connection.close()
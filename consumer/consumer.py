#!/usr/bin/env python
import pika
import time
import os
import sys


server = os.environ.get('RABBITMQ_HOST')
queue = os.environ.get('RABBITMQ_QUEUE')
sleep_time = float(os.environ.get('CONSUMER_SLEEP_TIME'))

print("Sleeping for 2 seconds..")
time.sleep(2)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=server))
channel = connection.channel()

channel.queue_declare(queue=queue, durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(sleep_time)
    sys.stdout.flush()
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue)

channel.start_consuming()
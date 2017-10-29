#!/usr/bin/env python
import pika
import os
import time

server = os.environ.get('RABBITMQ_HOST')
queue = os.environ.get('RABBITMQ_QUEUE')
sleep_time = float(os.environ.get('PRODUCER_SLEEP_TIME'))

print("Sleeping for 2 seconds..")
time.sleep(2)


connection = pika.BlockingConnection(pika.ConnectionParameters(host=server))
channel = connection.channel()

channel.queue_declare(queue=queue, durable=True)

i=0
while True:
    #message = ' '.join(sys.argv[1:]) or "Hello World!"
    message = "Message " + str(i)

    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=message,
                          properties=pika.BasicProperties(
                             delivery_mode = 2, # make message persistent
                          ))
    print(" [x] Sent %r" % message)
    i = i+1
    time.sleep(sleep_time)

connection.close()
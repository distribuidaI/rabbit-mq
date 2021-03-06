#!/usr/bin/env python3
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                        # make message persistent
                        delivery_mode=2,
                      ))
print(" [x] Sent %r" % message)
connection.close()

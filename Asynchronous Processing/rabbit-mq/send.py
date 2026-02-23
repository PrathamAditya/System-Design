import pika
credentials = pika.PlainCredentials('root', 'root')

parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='This is the body of the third message.')
print(" [x] Sent 'Hello World!'")
connection.close()
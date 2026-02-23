# RabbitMQ (Docker + Pika)

This is a small local setup where I configured RabbitMQ using Docker 
and connected to it using Python (pika client).

RabbitMQ is running locally via docker-compose with the management plugin enabled.
Data is persisted using a dedicated Docker volume.

I created two simple scripts:

- send/ → acts as a producer and publishes messages to a queue
- receive/ → acts as a consumer and listens to the same queue

The producer sends a message to RabbitMQ.
The consumer receives and prints it in the terminal.

This is a minimal example to understand how:
- RabbitMQ works
- AMQP(Advanced Message Queuing Protocal) communication happens (pika<-> speaks this language over TCP)
- Producer and Consumer interact


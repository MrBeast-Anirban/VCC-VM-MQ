from fastapi import FastAPI
import pika, json

app = FastAPI()

# RabbitMQ connection details
RABBITMQ_HOST = "192.168.100.5"  # Replace with correct RabbitMQ VM IP
RABBITMQ_USER = "myuser"  # Default username
RABBITMQ_PASS = "mypassword"  # Default password

# Establish connection with credentials
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
parameters = pika.ConnectionParameters(RABBITMQ_HOST, credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

@app.post("/send/")
def send_message(message: str):
    body = json.dumps({"message": message})
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=body,
        properties=pika.BasicProperties(delivery_mode=2)  # Makes message persistent
    )
    return {"status": "Message sent"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

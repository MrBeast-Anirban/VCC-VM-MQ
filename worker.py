import pika, json, psycopg2

# Connect to RabbitMQ
RABBITMQ_HOST = "localhost"
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue="task_queue", durable=True)

# Connect to PostgreSQL
DB_HOST = "192.168.100.7"  # VM3's IP
DB_NAME = "microservices"
DB_USER = "micro_user"
DB_PASS = "password"

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST
)
cur = conn.cursor()

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received: {message['message']}")
    
    # Insert into database
    cur.execute("INSERT INTO messages (content) VALUES (%s)", (message['message'],))
    conn.commit()
    
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue="task_queue", on_message_callback=callback)
print("Waiting for messages...")
channel.start_consuming()

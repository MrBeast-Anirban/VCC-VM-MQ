# Microservices-Based Messaging queue Architecture using FastAPI, RabbitMQ, and PostgreSQL

## Project Overview

This project demonstrates a microservices-based architecture using three Virtual Machines (VMs) for different services:
- VM1 (API Service) – FastAPI-based microservice that sends messages.
- VM2 (Message Queue) – RabbitMQ for message brokering.
- VM3 (Database Service) – PostgreSQL for data storage.
The microservices communicate through RabbitMQ, enabling asynchronous message passing.

### IP addresses as per my system (internal communication subnet)
- VM1 (192.168.100.6) – FastAPI app to send messages.
- VM2 (192.168.100.5) – RabbitMQ server for message queuing.
- VM3 (192.168.100.7) – PostgreSQL database for storing messages.

### Install the below dependencies on all virtual machines
- sudo apt update && sudo apt upgrade -y
- sudo apt install python3 python3-pip -y
- python3 -m venv myenv
- source myenv/bin/activate
- pip install fastapi uvicorn requests pika psycopg2

### On VM2 (RabbitMQ Server)
- sudo apt install rabbitmq-server -y
- sudo systemctl enable rabbitmq-server
- sudo systemctl start rabbitmq-server
- sudo rabbitmqctl add_user user password
- sudo rabbitmqctl set_permissions -p / user ".*" ".*" ".*"

### On VM3 (PostgreSQL Server)
- sudo apt install postgresql postgresql-contrib -y
- sudo systemctl start postgresql
- sudo systemctl enable postgresql
- sudo -i -u postgres
- psql

### Inside PostgreSQL shell, create a database and user as per your requirements.

## Test the Microservices

### Start FastAPI API Gateway on VM1:
python3 app.py

### Start the Worker Service on VM2:
python3 worker.py

### Send a Request from VM1 to the API Gateway:
- curl -X POST "http://192.168.100.5:8000/send/" -H "Content-Type: application/json" -d '{"message": "Hi There I am doing Assignment!"}'

### Check if Worker Service Receives the Message (VM2)
If successful, it will print:
- - Received: Hi There I am doing Assignment!

### Verify Data in PostgreSQL (VM3)
- sudo -u postgres psql -d microservices
- SELECT * FROM messages;



This project successfully implements a microservices-based architecture using FastAPI, RabbitMQ, and PostgreSQL across multiple VMs. The architecture ensures scalability, modularity, and efficient inter-service communication.
Future enhancements could include:
- Containerization with Docker
- Service orchestration using Kubernetes
- Logging & monitoring integration
This serves as a foundation for scalable distributed applications in real-world scenarios.

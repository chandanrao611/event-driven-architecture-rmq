The Producer Service is responsible for publishing messages to RabbitMQ. It receives requests from FastAPI endpoints and sends events to RabbitMQ exchanges for consumption by downstream services.

**Technology Stack**

Python 3.10+

FastAPI

RabbitMQ

Pika

Uvicorn

**Installation**

pip install fastapi uvicorn pika python-dotenv

**Activate Virtual Environment**

venv\Scripts\activate

**Run Application**

uvicorn main:app --reload --port 3000



<img width="592" height="527" alt="image" src="https://github.com/user-attachments/assets/eaf0f60d-9ce8-47ec-a5ef-7fcc8e96f022" />

**Producer Service** (orders repo)

<img width="687" height="485" alt="image" src="https://github.com/user-attachments/assets/c61b383f-6405-4788-ad85-2f5dc6bef2e1" />

**Consumer Service** (notifications repo)

<img width="641" height="435" alt="image" src="https://github.com/user-attachments/assets/6af3b3de-9b2f-4bb5-88dd-2fe31bbe881f" />

<img width="1362" height="512" alt="image" src="https://github.com/user-attachments/assets/9d8a95d1-d917-4fad-ae53-e34f424de5c2" />


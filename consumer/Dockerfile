FROM python:3.11-slim

WORKDIR /app

COPY consumer.py .

RUN pip install kafka-python

EXPOSE 5002

CMD ["python", "consumer.py"]
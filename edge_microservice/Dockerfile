FROM python:3.11-slim

WORKDIR /app

COPY edge_microservice.py .

RUN pip install flask kafka-python

EXPOSE 5001

CMD ["python", "edge_microservice.py"]
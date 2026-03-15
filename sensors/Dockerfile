FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*

COPY sensor_data_stream.py .

RUN pip install requests

EXPOSE 5000

CMD ["python", "sensor_data_stream.py"]
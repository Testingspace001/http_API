# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./src
EXPOSE 8080
CMD ["python", "./src/Http_Api.py"]
CMD ["python", "./src/Test_Http_api.py"]




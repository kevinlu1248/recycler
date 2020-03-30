# Dockerfile
FROM python:3.7
COPY /server /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
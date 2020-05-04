# Dockerfile
FROM python:3.7
COPY . /app
WORKDIR /app
ENV GOOGLE_CLOUD_STORAGE_ACCESS_KEY=GOOG1E47RGW7AVKTVUZWR7O4OPBJK7NGNBCOOZDSO5ZCCJ2VR6KHKWCQTDVFI GOOGLE_CLOUD_STORAGE_SECRET_KEY=O3yyiIsg3LVPzj8XOcbKLm1L6YLrUtqVOAM7siLC GOOGLE_CLOUD_STORAGE_BUCKET=https://console.cloud.google.com/storage/browser/recycler/test_images MAIN_BUCKET=recycler PROJECT_ID=recycler-7dc49 REGION_NAME=us-central1 DATASET_ID=ICN3650956947332530176
# RUN pip install -r requirements.txt
RUN pip install Flask Pillow tensorflow keras gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app

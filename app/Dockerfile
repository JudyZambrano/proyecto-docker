FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir psycopg2-binary redis
COPY app.py .
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]

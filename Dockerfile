FROM python:3.11-slim AS dependencies
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM dependencies AS test
WORKDIR /app
COPY . .
RUN pytest addition-service/app/tests/

FROM dependencies AS production
WORKDIR /app
COPY addition-service/ ./addition-service/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["python", "addition-service/app.py"]
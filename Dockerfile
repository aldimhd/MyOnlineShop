FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
  && rm -rf /var/lib/apt/lists/*

# create runtime directories for sqlite, static, and media
RUN mkdir -p /app/data /app/staticfiles /app/media

COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

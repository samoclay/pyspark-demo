FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y default-jdk \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pyspark pylint

COPY . .

CMD ["spark-submit", "--master", "local[*]", "job.py"]

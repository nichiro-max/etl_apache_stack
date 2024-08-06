FROM bitnami/spark:latest

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pyspark confluent_kafka

ENTRYPOINT ["spark-submit", "--master", "spark://spark:7077", "app/spark_etl.py"]
# Spark ETL Pipeline Project

## Overview

This project demonstrates a production-grade ETL (Extract, Transform, Load) pipeline using Apache Spark, Apache Kafka, Apache Airflow, and Delta Lake. It is designed to showcase the capabilities of these technologies in a real-world data processing scenario.

## Project Components

1. **Apache Spark**: Used for large-scale data processing and transformations.
2. **Apache Kafka**: Serves as the message broker for streaming data.
3. **Apache Airflow**: Manages and orchestrates the ETL workflow.
4. **Delta Lake**: Provides ACID transactions and scalable metadata handling on top of Apache Spark.

## Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Docker Compose**: Required to manage multi-container Docker applications.
- **Python**: Required for running Apache Airflow.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/nichiro-max/etl_apache_stack.git
cd etl_apache_spark-main
```

### Configure Docker

Ensure that the `docker-compose.yml` file is correctly configured for your environment. The default configuration uses `wurstmeister/kafka`, `zookeeper:3.8`, `bitnami/spark`, and `apache/airflow:2.7.0`.

### Build and Start the Docker Containers

```bash
docker-compose up -d
```

This command will start all necessary services: Zookeeper, Kafka, Spark, and Airflow.

### Check Container Status

Verify that the containers are running:

```bash
docker ps
```

### Access Airflow

Airflow's web interface will be available at `http://localhost:8081`. You can access it to manage and monitor your DAGs.

### Kafka Topics

The Kafka topic used in this project is `events`. You can create and manage topics using the Kafka command-line tools.

### Spark Job

The Spark job will consume data from Kafka, transform it, and store it into Delta Lake. Ensure your Spark job configuration is correct in the Docker setup.

## Directory Structure

- `docker-compose.yml`: Docker Compose configuration file.
- `app/`: Contains Spark job scripts and configuration.
- `dags/`: Apache Airflow DAGs for managing the ETL workflow.
- `airflow_logs/`: Directory for Airflow logs.
- `README.md`: Project documentation.

## Usage

1. **Stream Data**: Use Kafka to produce streaming data to the `events` topic.
2. **Process Data**: Apache Spark will consume the data from Kafka, process it, and write it to Delta Lake.
3. **Orchestrate**: Apache Airflow will manage the ETL workflow and ensure that the data pipeline runs as expected.

## Troubleshooting

- **Zookeeper or Kafka Issues**: Check logs using `docker logs <container_name>` for detailed error messages.
- **Permission Errors**: Ensure Docker has appropriate file permissions.

## Contributing

Feel free to fork the repository, create a branch for your feature or fix, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

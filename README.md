Ariflow
=======

How to run
----------
```bash
docker compose up
```
- run with flower
    ```bash
    docker-compose --profile flower up
    ```
- run with airflow-cli
    ```bash
    docker-compose --profile debug up
    ```

How to cleanup
--------------
```bash
docker compose down --volumes
```

Guide & `docker-compose.yaml`
-----------------------------
- https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#

How to install `apache-airflow`
-------------------------------
- https://airflow.apache.org/docs/apache-airflow/stable/start.html
    ```bash
    AIRFLOW_VERSION=2.4.2
    PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
    CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

    pip install apache-airflow-providers-postgres
    ```


from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def _t1(ti):
    ti.xcom_push(key="xcom_key", value="Hello, Ariflow!")


def _t2(ti):
    val = ti.xcom_pull(key="xcom_key", task_ids="t1")
    print(f"xcom value: '{val}'")


with DAG(
    "dag_xcom",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id="t1", python_callable=_t1)

    t2 = PythonOperator(task_id="t2", python_callable=_t2)

    t1 >> t2

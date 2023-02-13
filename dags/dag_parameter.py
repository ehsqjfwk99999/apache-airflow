import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator


def _print_params(**context):
    params = context["templates_dict"]
    print(f"dag: {params['dag']}")
    print(f"task: {params['task']}")
    print(f"task_instance: {params['task_instance']}")
    print(f"ds: {params['ds']}")
    print(f"ds_nodash: {params['ds_nodash']}")


with DAG(
    "dag_parameter",
    start_date=dt.datetime(2023, 1, 1),
    schedule_interval="* * * * *",
    catchup=False,
) as dag:

    print_params = PythonOperator(
        task_id="print_params",
        python_callable=_print_params,
        templates_dict={
            "dag": "{{dag}}",
            "task": "{{task}}",
            "task_instance": "{{task_instance}}",
            "ds": "{{ds}}",
            "ds_nodash": "{{ds_nodash}}",
        },
    )

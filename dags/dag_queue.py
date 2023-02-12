import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "dag_queue",
    start_date=dt.datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    # use default queue
    t1 = BashOperator(task_id="t1", bash_command="sleep 3")

    # use external queue (created in worker-2)
    t2 = BashOperator(task_id="t2", queue="high_cpu", bash_command="sleep 6")

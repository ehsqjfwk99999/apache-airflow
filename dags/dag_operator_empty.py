import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

# EmptyOperator: https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/empty/index.html


with DAG(
    "dag_operator_empty",
    start_date=dt.datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = EmptyOperator(task_id="empty")

    t2 = BashOperator(task_id="echo", bash_command="sleep 3")

    t1 >> t2

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


def _t1_1(ti):
    ti.xcom_push(key="xcom_key", value=123)


def _t2(ti):
    ti.xcom_pull(key="xcom_key", task_ids="t1")


def _branch(ti):
    value = ti.xcom_pull(key="xcom_key", task_ids="t1")
    if value == 42:
        return "t2"

    return "t3"


with DAG(
    "dag_trigger",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1_1 = BashOperator(task_id="t1_1", bash_command="sleep 3")
    t1_2 = BashOperator(task_id="t1_2", bash_command="sleep 6")
    t1_3 = BashOperator(task_id="t1_3", bash_command="sleep 9")

    t2 = BashOperator(
        task_id="t2", bash_command="echo 'all success'", trigger_rule="all_success"
    )

    [t1_1, t1_2, t1_3] >> t2

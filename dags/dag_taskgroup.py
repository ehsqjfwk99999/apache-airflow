from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup


def tg1():

    with TaskGroup("tg1", tooltip="Task group 1") as group:

        tg1_t1 = BashOperator(task_id="tg1_t1", bash_command="sleep 9")

        tg1_t2 = BashOperator(task_id="tg1_t2", bash_command="sleep 6")

        tg1_t3 = BashOperator(task_id="tg1_t3", bash_command="sleep 3")

    return group


def tg2():

    with TaskGroup("tg2", tooltip="Task group 2") as group:

        tg2_t1 = BashOperator(task_id="tg2_t1", bash_command="sleep 3")

        tg2_t2 = BashOperator(task_id="tg2_t2", bash_command="sleep 6")

        tg2_t3 = BashOperator(task_id="tg2_t3", bash_command="sleep 9")

    return group


with DAG(
    "dag_taskgroup",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = tg1()

    t2 = BashOperator(task_id="t2", bash_command="sleep 3")

    t3 = tg2()

    t1 >> t2 >> t3

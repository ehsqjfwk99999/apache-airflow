import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator


def _t1(ti):
    ti.xcom_push(key="xcom_key", value=True)


def _branch(ti):
    value = ti.xcom_pull(key="xcom_key", task_ids="t1")

    if value:
        return "t2_true"
    else:
        return "t3_false"


with DAG(
    "dag_branch",
    start_date=dt.datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id="t1", python_callable=_t1)

    branch = BranchPythonOperator(task_id="branch", python_callable=_branch)

    t2_true = BashOperator(task_id="t2_true", bash_command="echo 'xcom: True'")
    t2_false = BashOperator(task_id="t2_false", bash_command="echo 'xcom: False'")

    t1 >> branch >> [t2_true, t2_false]

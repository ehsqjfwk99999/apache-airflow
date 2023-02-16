import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator

# https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html

# passed like (conf=..., dag=...) to **context
def _show_context_variables(**context):
    print(context)


def _only_execution_date(execution_date):
    print(execution_date)


def _pass_by_op_args(msg, **context):
    print(msg)


def _pass_by_op_kwargs(**context):
    print(context["message"])


def _pass_by_template_dict(**context):
    params = context["templates_dict"]
    print(f"dag: {params['dag']}")
    print(f"task: {params['task']}")
    print(f"task_instance: {params['task_instance']}")
    print(f"ds: {params['ds']}")
    print(f"ds_nodash: {params['ds_nodash']}")


with DAG(
    "dag_pythonoperator",
    start_date=dt.datetime(2023, 1, 1),
    schedule_interval="* * * * *",
    catchup=False,
) as dag:

    show_context_variables = PythonOperator(
        task_id="show_context_variables",
        python_callable=_show_context_variables,
    )

    only_execution_date = PythonOperator(
        task_id="only_execution_date",
        python_callable=_only_execution_date,
    )

    pass_by_op_args = PythonOperator(
        task_id="pass_by_op_args",
        python_callable=_pass_by_op_args,
        op_args=["message passed by op_args"],
    )

    pass_by_op_kwargs = PythonOperator(
        task_id="pass_by_op_kwargs",
        python_callable=_pass_by_op_kwargs,
        op_kwargs={"message": "message passed by op_kwargs"},
    )

    pass_by_template_dict = PythonOperator(
        task_id="pass_by_template_dict",
        python_callable=_pass_by_template_dict,
        templates_dict={
            "dag": "{{dag}}",
            "task": "{{task}}",
            "task_instance": "{{task_instance}}",
            "ds": "{{ds}}",
            "ds_nodash": "{{ds_nodash}}",
        },
    )

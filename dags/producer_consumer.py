import datetime as dt

from airflow import DAG, Dataset
from airflow.decorators import task

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

with DAG(
    dag_id="pc_producer",
    schedule="@daily",
    start_date=dt.datetime(2023, 1, 1),
    catchup=False,
):

    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, "a+") as f:
            f.write("producer update")

    @task(outlets=[my_file_2])
    def update_dataset_2():
        with open(my_file_2.uri, "a+") as f:
            f.write("producer update")

    update_dataset()
    update_dataset_2()

with DAG(
    dag_id="pc_consumer",
    schedule=[my_file, my_file_2],
    start_date=dt.datetime(2023, 1, 1),
    catchup=False,
):

    @task
    def read_dataset():
        with open(my_file.uri, "r") as f:
            print(f.read())

    read_dataset()

# 2)
# Implement a DAG that prints "Hello World!" every hour:
#   a) using python;
#   b) using bash.

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define function to print "Hello World!"
def print_hello_world():
    print("Hello World!")

# Define the default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 15),
    "retries": 0,
    "retry_delay": timedelta(minutes = 5),
}

# Define the DAG
dag = DAG(
    "hello_world_python",
    default_args = default_args,
    description = "Print Hello World every hour",
    schedule = timedelta(hours = 1),
)

# Define the task to print "Hello World!" using PythonOperator
print_hello_task = PythonOperator(
    task_id = "print_hello_world",
    python_callable = print_hello_world,
    dag = dag,
)
# 3) Implement a DAG with two tasks:
# A → B
# - set the dag_id as "Sequential tasks";
# - set the start date to the past, and catchup to True;
# - Task A uses PythonOperator to print "This is from Task A";
# - Task B uses BashOperator to echo "This is from task B";
# - use the Airflow GUI to check on the running tasks.

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

def print_hello():
    print("This is from Task A")

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 15),
    "retries": 1,
    "retry_delay": timedelta(minutes = 5),
    "catchup": True,
}

dag = DAG(
    "SequentialTasks",
    default_args = default_args,
    schedule = timedelta(days = 1),
)

task_a = PythonOperator(
    task_id = "task_a",
    python_callable = print_hello,
    dag = dag,
)

task_b = BashOperator(
    task_id = "task_b",
    bash_command = 'echo "This is from task B"',
    dag = dag,
)

task_a >> task_b
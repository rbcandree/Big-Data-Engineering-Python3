# Implement a DAG that decides between two tasks based on which day of the week it currently is. 
# If it is a working day we run a task that prints "Gotta work" and 
# if it's saturday or sunday we run a task that prints "It's weekend". 
# Use branching to choose between these two tasks. 
# You may find datetime.today().weekday() to be useful here.

from airflow.models import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime

def print_working_day():
    print("Gotta work")

def print_weekend():
    print("It's weekend")

def task_option():
    current_day = datetime.today().weekday()
    # 0-4 -> Mon-Fri; 5-6 -> Sat-Sun
    if current_day < 5:
        return print_working_day
    else:
        return print_weekend

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 28),
    "retries": 1,
    "catchup": False,
}

dag = DAG(
    "Working_day_or_weekend_DAG",
    default_args = default_args,
    schedule = "@daily",
)

with dag:
    # Task to decide which function to execute
    decide = BranchPythonOperator(
        task_id = "task_option",
        python_callable = task_option,
    )

    work = PythonOperator(
        task_id = 'working_day_task',
        python_callable = print_working_day,
    )

    weekend = PythonOperator(
        task_id='weekend_task',
        python_callable = print_weekend,
    )

    # Set task dependencies
    decide >> [work, weekend]
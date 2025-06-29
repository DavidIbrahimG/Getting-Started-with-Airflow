from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define task functions
def start_number(**context):
    context['ti'].xcom_push(key='number', value=10)
    print("Starting number is 10")

def add_five(**context):
    number = context['ti'].xcom_pull(key='number', task_ids='start_number')
    result = number + 5
    context['ti'].xcom_push(key='result', value=result)
    print(f"Added 5: {result}")

def multiply_by_two(**context):
    result = context['ti'].xcom_pull(key='result', task_ids='add_five')
    result *= 2
    context['ti'].xcom_push(key='result', value=result)
    print(f"Multiplied by 2: {result}")

def subtract_three(**context):
    result = context['ti'].xcom_pull(key='result', task_ids='multiply_by_two')
    result -= 3
    context['ti'].xcom_push(key='result', value=result)
    print(f"Subtracted 3: {result}")

def complete_square(**context):
    result = context['ti'].xcom_pull(key='result', task_ids='subtract_three')
    result = result ** 2
    print(f"Completed square: {result}")

# Define the DAG
with DAG(
    dag_id='maths_operation',
    start_date=datetime(2023, 10, 1),
    schedule='@daily',
    catchup=False
) as dag:

    # Define tasks
    start_task = PythonOperator(
        task_id='start_number',
        python_callable=start_number,
    )

    add_task = PythonOperator(
        task_id='add_five',
        python_callable=add_five,
    )

    multiply_task = PythonOperator(
        task_id='multiply_by_two',
        python_callable=multiply_by_two,
    )

    subtract_task = PythonOperator(
        task_id='subtract_three',
        python_callable=subtract_three,
    )

    complete_square_task = PythonOperator(
        task_id='complete_square',
        python_callable=complete_square,
    )

    # Set task dependencies
    start_task >> add_task >> multiply_task >> subtract_task >> complete_square_task

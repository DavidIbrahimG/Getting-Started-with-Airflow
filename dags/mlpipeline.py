from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Define our task function
def preprocess_data():
    print("Preprocessing data...")

# Define task 2
def train_model():
    print("Training model...")

# Define task 3
def evaluate_model():
    print("Evaluating model...")

# Define the DAG
with DAG(
    dag_id='ml_pipeline',
    start_date=datetime(2023, 10, 1),
    schedule='@weekly'
) as dag:

    # Define tasks
    preprocess_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data,
    )

    train_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )

    evaluate_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
    )

    # Set task dependencies
    preprocess_task >> train_task >> evaluate_task
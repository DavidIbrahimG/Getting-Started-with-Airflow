from airflow import DAG
from airflow.decorators import task
from datetime import datetime

# Define the DAG
with DAG(
    dag_id = 'maths_sequence_dag_with_taskflow_api',
    start_date = datetime(2023, 10, 1),
    schedule = '@once',
    catchup = False
) as dag:
    # task 1: start with a number
    @task
    def start_number():
        initial_number = 10
        print(f"Starting with number: {initial_number}")
        return initial_number
    
    # task 2: add 5 to the number
    @task
    def add_five(number):
        result = number + 5
        print(f"Adding 5: {result}")
        return result
    
    # task 3: multiply the result by 2
    @task
    def multiply_by_two(number):
        result = number * 2
        print(f"Multiplying by 2: {result}")
        return result
    
    # task 4: subtract 3 from the result
    @task
    def subtract_three(number):
        result = number - 3
        print(f"Subtracting 3: {result}")
        return result
    
    # task 5: complete the square by squaring the result
    @task
    def complete_square(number):
        result = number ** 2
        print(f"Completed square: {result}")
        return result
    
    # Define the task dependencies
    initial = start_number()
    added = add_five(initial)
    multiplied = multiply_by_two(added)
    subtracted = subtract_three(multiplied)
    squared = complete_square(subtracted)   



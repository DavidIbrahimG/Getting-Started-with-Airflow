# 🧮 Airflow Math Operations DAG

This project demonstrates a simple Apache Airflow DAG that performs a sequence of basic mathematical operations using `PythonOperator`.

## 📌 Overview

The DAG consists of 5 tasks executed in sequence:

1. **Start Number** – Initializes the value to `10`.
2. **Add Five** – Adds 5 to the initial number.
3. **Multiply by Two** – Multiplies the result by 2.
4. **Subtract Three** – Subtracts 3 from the new value.
5. **Complete Square** – Squares the final result.

Each task passes its result to the next using **XComs**, showcasing how data can flow between tasks in Airflow.

## 🚀 Getting Started

1. Ensure you have Airflow installed and initialized.
2. Copy the DAG file (`mlpipeline.py`) into your Airflow `dags/` directory.
3. Start the Airflow scheduler and webserver:
   ```bash
   airflow scheduler
   airflow webserver

4. Trigger the DAG manually or let it run on its defined schedule (@daily).

### 🛠 Requirements
    Python 3.7+

    Apache Airflow 2.x or 3.x

📌 Note: Remove provide_context=True if you're on Airflow 2+ or later — context is passed automatically.

### 📂 Project Structure
    airflowastro/
    ├── dags/
    │   ├── __pycache__/
    │   ├── exampledag.py
    │   ├── maths_operation.py
    │   ├── mlpipeline.py
    │   └── taskflowapi.py
    ├── include/
    ├── plugins/
    ├── tests/
    ├── .airflowignore
    ├── .dockerignore
    ├── .env
    ├── .gitignore
    ├── airflow_settings.yaml
    ├── Dockerfile
    ├── packages.txt
    ├── README.md
    └── requirements.txt

### 📖 Concepts Illustrated
* Task orchestration using Airflow

* Data passing with XComs

* Use of PythonOperator

* DAG scheduling and dependencies


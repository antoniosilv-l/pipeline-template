# import the libraries

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Ramesh Sannareddy',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='sample-etl-dag',
    default_args=default_args,
    description='Sample ETL DAG using bash',
    schedule_interval=timedelta(days=1),
)

extract = BashOperator(
    task_id='extract',
    bash_command='echo "extract"',
    dag=dag
)

transform = BashOperator(
    task_id='transform',
    bash_command='echo "transform"',
    dag=dag,
)

load = BashOperator(
    task_id='load',
    bash_command='echo "load"',
    dag=dag,
)

extract >> transform >> load
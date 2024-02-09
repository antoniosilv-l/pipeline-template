from airflow.decorators import dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime, timedelta

import sqlite3

default_args = {
    'owner': 'asilva',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


@dag(
    'call_sqlite',
    description=''' DAG para testar a utilização do SQLOperator. ''',
    start_date=datetime(2024, 2, 8), 
    max_active_runs=2, 
    schedule='@daily', 
    default_args=default_args, 
    catchup=False,
)
def select_table():
    slc_table1 = SQLExecuteQueryOperator(
        task_id='select_table1',
        conn_id='sqlite',
        sql='select * from customer'
    )

    slc_table2 = SQLExecuteQueryOperator(
        task_id='select_table2',
        conn_id='sqlite',
        sql='select * from employee'
    )

    slc_table1 >> slc_table2

select_table()
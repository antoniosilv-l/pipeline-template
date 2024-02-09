from airflow.decorators import dag, task
from airflow.hooks.base import BaseHook
from datetime import datetime, timedelta

import sqlite3

default_args = {
    'owner': 'asilva',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

@task
def pega_conexao():
    connection = BaseHook.get_connection('sqlite')
    connection = connection.host
    
    return connection

@task
def explora_tabela(host):

    conn = sqlite3.connect(host)
    cursor = conn.cursor()

    tabelas = cursor.execute("""select distinct tbl_name from sqlite_schema""")
    
    for tabela in tabelas:
        print(f'\n{tabela}')


@dag(
    dag_id='sqlite_explorer',
    description=''' Exploração de dados e CRUD no sqlite. ''',
    default_args=default_args,
    start_date=datetime(2024, 2, 8),
    schedule='@daily',
    max_active_runs= 2,
    catchup=False,
    tags=['sqlite', 'python'],
)
def exploracao():
    results1 = pega_conexao()
    results1

    results = explora_tabela(results1)
    results

    results1 >> results

exploracao()


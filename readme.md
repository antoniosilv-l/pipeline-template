# Pipeline de Dados  🎢

Projeto voltado para o estudo e criação de um pipeline local end-to-end.

Após a configuração teste e aprendizado local, migraremos a solução para um ambiente docker, onde será mais facil ser reproduzido.


## Airflow 🌀

Para o processo de Extract and Load, vamos utilizar a solução do apache-airflow.

*Configuração*
```bash
# Localização da pasta home do airflow:
export AIRFLOW_HOME=caminha_da_pasta

# Instalação do airflow:
# Seguindo a documentação optei por fazer a instalação via CONSTRAINT.
AIRFLOW_VERSION=2.7.3

PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}
```

*Inicializando o Airflow*

```bash
# Iniciando o banco de dados
airflow db migrate

# Variavel para conexão ao banco de dados.
# Para segurança optei por utilizar a variavel 
# AIRFLOW__DATABASE__SQL_ALCHEMY_CONN para passar a informação do banco de dados.

export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sql_alchemy_conn

# Criando o usuario admin
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

# Iniciando o webserver e scheduler
airflow webserver --port 8080

airflow scheduler
```

## dbt 🗝️
# Pipeline de Dados  🎢

Projeto voltado para o estudo e criação de um pipeline local end-to-end.

Após a configuração teste e aprendizado local, migraremos a solução para um ambiente docker, onde será mais facil ser reproduzido.


## Airflow 🌀

Para o processo de Extract and Load, vamos utilizar a solução do apache-airflow.

Após seguir o processo de instalação contido na documentação do airflow, podemos iniciar.

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
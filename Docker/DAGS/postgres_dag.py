from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

# Define the PostgreSQL connection details
postgres_conn_id = 'postgres_conn'
postgres_table = 'assignment_table'

# Function to create the table if it doesn't exist
def create_table_if_not_exists():
    postgres_hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    create_table_query = f"CREATE TABLE IF NOT EXISTS {postgres_table} (execution_time TIMESTAMP)"
    postgres_hook.run(create_table_query)

# Function to add an entry to the PostgreSQL database
def add_entry_to_db():
    postgres_hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    execution_time = datetime.now()
    insert_query = f"INSERT INTO {postgres_table} (execution_time) VALUES ('{execution_time}')"
    postgres_hook.run(insert_query)

# Define the DAG
dag = DAG(
    'add_entry_dag',
    description= 'DAG to add entry to PostgreSQL database',
    schedule_interval = '*/1 * * * *',  # Execute every 1 minutes
    start_date = datetime(2023, 1, 1),  # Replace with the desired start date
    catchup = False
)

# Define the tasks
create_table_task = PythonOperator(
    task_id='table_creation_task',
    python_callable=create_table_if_not_exists,
    dag=dag
)

add_entry_task = PythonOperator(
    task_id='add_entry_task',
    python_callable=add_entry_to_db,
    dag=dag
)


create_table_task >> add_entry_task
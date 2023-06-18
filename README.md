# Docker_Kubernates

## Docker

* A Directed Acyclic Graph (DAG) 'add_entry_dag' was created, which represents a workflow or a series of tasks to be executed.

* The schedule_interval for the DAG was set to daily, indicating that the tasks within the DAG will be executed once every day.

```
dag = DAG(
    'add_entry_dag',
    description= 'DAG to add entry to PostgreSQL database',
    schedule_interval = '*/1 * * * *',  # Execute every 1 minutes
    start_date = datetime(2023, 1, 1),  # Replace with the desired start date
    catchup = False
)
```

* The first task, named "table_creation_task," was created. This task utilizes the Python Operator with PostgresHook, a component that         interacts with a Postgres database. The task is responsible for creating a table in the database. The connection to the Postgres database   is established using the "postgres_conn_id" parameter, which is set to "postgres".

```
create_table_task = PythonOperator(
    task_id='table_creation_task',
    python_callable=create_table_if_not_exists,
    dag=dag
)
```

* The second task, named "add_entry_task," was created. This task also uses the Python Operator and PostgresHook. Its purpose is to           insert values into the table previously created in the database.

```
add_entry_task = PythonOperator(
    task_id='add_entry_task',
    python_callable=add_entry_to_db,
    dag=dag
)

```

* Finally, the dependencies between the tasks were established. This means that the tasks were linked in a specific order to ensure they are   executed sequentially. For example, "table_creation_task" must be completed before "add_entry_task. These dependencies ensure that the       tasks are executed in the desired sequence to achieve the intended workflow.

```
create_table_task >> add_entry_task
```

* Dag with two tasks
<img width="513" alt="Dags" src="https://github.com/PankajKrSingh7/Docker-Kubernates/assets/54628129/c1c7d6fb-0c69-49ee-9e5b-3d329ef342ab">


* Table created with imestamp values
<img width="315" alt="table_entries_1" src="https://github.com/PankajKrSingh7/Docker-Kubernates/assets/54628129/6e7de214-b063-4609-9dcb-fc82d1566f39">





## Kubernates

* Installed minikube.

```
  brew install minikube
  minikube start
```

* Created a postgres-deployment.yaml and made a pod using kubectl.
```
kubectl apply -f postgres-deployment.yaml
```

* Added dependencies of python and airflow in a postgres image by using the following commands inside the postgres pod. 
```
apt-get -y update
apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget 
wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
tar -xf Python-3.7.12.tgz
cd /Python-3.7.12
./configure --enable-optimizations
make -j $(nproc)
make altinstall
# STEPS TO INSTALL AIRFLOW VERSION 2.5.0
apt-get install libpq-dev
pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql://airflow:airflow@localhost:5432/airflow
airflow db init
airflow users create -u airflow -p airflow -f pankaj -l singh -e pankajchbs007@gmial.com -r Admin
```
* Made a postgres-service.yaml and created a service using
```
kubectl apply -f postgres-service.yaml
```

* Made a airflow-deployment.yaml and created a deployment using
```
kubectl apply -f airflow-deployment.yaml
```

* Made a airflow-service.yaml and created a service using
```
kubectl apply -f airflow-service.yaml
```

* Created a DAG and postgres connection and ran it to get the entries in a postgres table.

* Accessed the airflow webserver by running the command minikube service airflow. My airflow is accessible on http://127.0.0.1:54868 Upon logging in, the dag was visible, then created a postgres connection and then ran my dag, it has been succesfully executed.

<img width="554" alt="kubernates-airflow" src="https://github.com/PankajKrSingh7/Docker-Kubernates/assets/54628129/e4b1cacb-5c27-4c72-8c9e-a0b3fb64e825">

* Dags

<img width="396" alt="dags_2" src="https://github.com/PankajKrSingh7/Docker-Kubernates/assets/54628129/971f856e-fef5-4de1-bcbe-5e2150e2df7e">

* Verified the entries in the table 
<img width="391" alt="table_entries_2" src="https://github.com/PankajKrSingh7/Docker-Kubernates/assets/54628129/13fb96eb-1dc6-4ebd-b06c-6ae07e6e07ab">


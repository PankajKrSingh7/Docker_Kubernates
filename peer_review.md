## Jaswin Approach

### Docker Task

1. First, he created a dag with two tasks. Then by using the docker-compose command, he started the airflow container. 
2. From webui he created a connection with Postgres.
3. Then he triggers the dag.

### Kubernetes Task
1. He created a custom docker image which contains the Postgres image and all the installation commands required to connect with airflow. This step is a little bit different from my process.
2. By using the Kubectl command he deployed the Postgres pod.
3. Then he started Postgres service.
4. Then he deployed the airflow pod and started the airflow service.
5. Now he created a dag in an airflow scheduler container.
6. Triggered the dag in Webui.

## Rajkeshav Review

### Docker Task

1. Similar to Jaswin, First he created a dag with two tasks. Then by using docker-compose, he started airflow containers.
2. From webui he created a connection with Postgres.
3. Then he triggers the dag.

## Kubernetes Task
1. In this task steps followed by Rajkeshav is very much similar to the steps I followed.
2. By using Kubectl he deployed the Postgres pod.
3. Then he installed all the requirements in the Postgres container.
4. Then he started Postgres service.
4. Then he deployed the airflow pod and started the airflow service.
5. Now he created dag in an airflow scheduler container.
6. Triggered the dag in Webui.

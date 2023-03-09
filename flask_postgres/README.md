# Flask & Postgres
## Run

### Python run
```
cd .\flask_postgres\
flask --app app run 
```


### Run with docker (with "HARDCODE")
```
# create custom network
docker network create mynetwork
# create docker container
docker build -t 6_back . 
# run docker container
docker run --rm -d --name database --network mynetwork -e POSTGRES_USER=docker_app -e POSTGRES_PASSWORD=docker_app -e POSTGRES_DB=docker_app_db postgres:14

# create table in db_base
docker exec -it database psql --username docker_app --dbname docker_app_db

CREATE TABLE app_table (  
id TEXT NOT NULL,         
text TEXT NOT NULL,       
status TEXT NOT NULL      
);                        

# run backend
docker run --rm -d --name backend --network mynetwork -p 8000:8000 -e HOST=database 6_back

# create row:
curl -X PUT localhost:8000/api -H 'Content-Type: application/json' -d '{"text":"Buy milk", "status":"active"}'
```
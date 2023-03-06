# Tg_bot with docker bild

## Description 
Project to study volume in docker


## Installation

``` shell
  
# clone repo:
git clone https://github.com/SashaMogilevskii/tg_bot_with_docker_bild.git


# create virtualenv:
virtualenv myenv

# activate virtualenv:
myenv/Scripts/activate


# create tg_token
# create .env file  and add your token in SECRET_TOKEN
#


# run tg_bot.py:
run main.py

```



## Command for build and run docker 
```shell
# build image docker
docker build -t tg_bot_files . 

# create volume
docker volume create tg_vol

# run image 
docker run --rm -d -p 8123:8123 -p 9000:9000 --name ch_db yandex/clickhouse-server

docker run --rm -d -e SECRET_TOKEN=<your_token> -v tg_vol:/app/todo_result tg_bot_files

# exec image
docker exec -it <image_names> bash


```
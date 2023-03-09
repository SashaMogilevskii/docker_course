from clickhouse_driver import Client
import os
connection = Client(
    host=os.environ.get("CH_HOST"),
    user="default",
    password="",
    port=9000,
    database="todo",
)

connection.execute("CREATE DATABASE todo")
connection.execute("""CREATE TABLE todo.todo (
id String,
text String,
status String
) engine = MergeTree() order by id """)

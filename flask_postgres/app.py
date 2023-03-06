from flask import Flask, jsonify, request, make_response

import psycopg2
import uuid
import os

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        port="5432",
        database="docker_app_db",
        user="docker_app",
        password="docker_app",
        host=os.environ.get("HOST"),

    )
    return conn


@app.route("/test", methods=["GET"])
def testing():
    return make_response(jsonify({"Test": "OK"}), 200)


@app.route("/test", methods=["GET"])
def get_record():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, text, status FROM app_table;")
        sql_data = cur.fetchall()
        cur.close()
        conn.close()
    except psycopg2.DatabaseError as e:
        return f"{e}", 500

    todo_data = []
    for data in sql_data:
        id_, text, status = data
        todo_data.append({"id": id_,
                          "text": text,
                          "status": status})

    res = make_response(jsonify(todo_data), 200)
    return res


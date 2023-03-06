import logging
import os

from clickhouse_driver import Client
import pandas as pd
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO
)

# your tg_bot tokenS
load_dotenv()
try:
    SECRET_TOKEN = os.getenv("SECRET_TOKEN")
except:
    SECRET_TOKEN = os.environ.get("SECRET_TOKEN")
assert SECRET_TOKEN is not None, "SECRET_TOKEN IS EMPTY!"

connection = Client(
    host="localhost",
    user="default",
    password="",
    port=9000,
    database="todo"
)



PATH_TO_TODO_TABLE = "todo_result/todo_list.csv"

bot = Bot(token=SECRET_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="all")
async def all_tasks(payload: types.Message):

    ch_all_data = connection.execute("SELECT * FROM todo.todo")

    await payload.reply(
        f"```{pd.DataFrame(ch_all_data, columns=['text', 'status']).to_markdown()}```",
        parse_mode="Markdown"
    )

@dp.message_handler(commands="add")
async def add_tasks(payload: types.Message):
    text = payload.get_args().strip()

    connection.execute(
        "INSERT INTO todo.todo (text, status) VALUES (%(text)s, %(status)s)",
        {"text":text, "status":"active"}

    )

    logging.info(f"Add new task - {text}")
    await payload.reply(f"Add new task - {text}",
                        parse_mode="Markdown")


@dp.message_handler(commands="done")
async def complete_task(payload: types.Message):
    text = payload.get_args().strip()

    connection.execute(
        "ALTER TABLE todo.todo UPDATE status = 'complete' WHERE text = %(text)s",
        {"text": text}
    )
    logging.info(f"Finished task - {text}")
    await payload.reply(f"Complete *{text}*",
                        parse_mode="Markdown")


if __name__ == "__main__":
    executor.start_polling(dp)

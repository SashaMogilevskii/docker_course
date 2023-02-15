import logging
import os

import pandas as pd
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

logging.basicConfig(
    format="%(levelname)s: %(actime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO
)


#your tg_bot token
load_dotenv()
SECRET_TOKEN = os.getenv("SECRET_TOKEN")
assert SECRET_TOKEN is not None, "SECRET_TOKEN is empty!"

PATH_TO_TODO_TABLE = "todo_result/todo_list.csv"



import logging
import os

import pandas as pd
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO
)

# your tg_bot token
load_dotenv()
SECRET_TOKEN = os.getenv("SECRET_TOKEN")
assert SECRET_TOKEN is not None, "SECRET_TOKEN IS EMPTY!"

PATH_TO_TODO_TABLE = "todo_result/todo_list.csv"

bot = Bot(token=SECRET_TOKEN)
dp = Dispatcher(bot)


def get_todo_data() -> pd.DataFrame:
    """
    :return: DataFrame with our data (csv)
    """
    return pd.read_csv(PATH_TO_TODO_TABLE)


@dp.message_handler(commands="all")
async def all_tasks(payload: types.Message):


    try:
        await payload.reply(f"```{get_todo_data().to_markdown()}```",
                            parse_mode="Markdown"
                            )
    except:
        await payload.reply(f"ToDo list is empty!",
                            parse_mode="Markdown"
                            )




@dp.message_handler(commands="add")
async def add_tasks(payload: types.Message):
    text = payload.get_args().strip()
    new_task = pd.DataFrame({"text": [text],
                             "status": ["active"]
                             })
    updates_tasks = pd.concat([get_todo_data(),
                               new_task],
                              ignore_index=True, axis=0)
    # Save
    updates_tasks.to_csv(PATH_TO_TODO_TABLE, index=False)

    logging.info(f"Add new task - {text}")
    await payload.reply(f"Add new task - {text}",
                        parse_mode="Markdown")


@dp.message_handler(commands="done")
async def complete_task(payload: types.Message):
    text = payload.get_args().strip()
    df = get_todo_data()
    df.loc[df.text == text, "status"] = "complete"

    # Save
    df.to_csv(PATH_TO_TODO_TABLE, index=False)

    logging.info(f"Finished task - {text}")
    await payload.reply(f"Complete *{text}*",
                        parse_mode="Markdown")


if __name__ == "__main__":
    executor.start_polling(dp)

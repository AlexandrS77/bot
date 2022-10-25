import telebot
from random import *

token = 'token'

bot = telebot.TeleBot(token)

HELP = """
/help - помощь.
/add - добавить задачу.
/show - показать все задачи.
/random - случайная задача."""

rnd_tsk = ['Сходить в магазин', 'Сделать 50 отжиманий', 'Убраться', 'Почитать книгу']
tasks = {}

def add_todo(date, task):
  if date in tasks:
      tasks[date].append(task)
  else:
      tasks[date] = [task]

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(rnd_tsk)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"

    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

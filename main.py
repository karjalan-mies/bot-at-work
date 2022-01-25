import logging
import os

from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters)
from telegram import ReplyKeyboardMarkup

print(os.environ['KHL_TOKEN'])
my_bot = Updater(os.environ['KHL_TOKEN'],
                 use_context=True)
dispatcher = my_bot.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def start(update, context):
    main_keyboard = ReplyKeyboardMarkup([['Конф. Запад', 'Конф. Восток'],
                                         ['КХЛ', 'ЦСКА']])
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Welcome to KHLbot!',
        reply_markup=main_keyboard)


def echo(update, context):
    text = 'ECHO: ' + update.message.text

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)


def unknown_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Sorry, I didn\'t understand that command.')


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
unknown_command_handler = MessageHandler(Filters.command, unknown_command)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(unknown_command_handler)
dispatcher.add_handler(echo_handler)

my_bot.start_polling()
my_bot.idle()

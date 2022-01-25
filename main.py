import logging
import os
import sqlite3

from telegram.ext import (Updater, CallbackContext, CommandHandler, 
                          ConversationHandler)
from telegram.ext.filters import Filters, MessageFilter
from telegram.ext import MessageHandler, Filters
from telegram.update import Update
from telegram import ReplyKeyboardMarkup

from viewing_the_khl_structure import show_division, show_teams


conn = sqlite3.connect('khl_base.db', check_same_thread=False)
cur = conn.cursor()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

updater = Updater(token=os.environ['KHL_TOKEN'],
use_context=True)
updater.start_polling()
dp = updater.dispatcher


def start(update: Update, context: CallbackContext):
    my_keyboard = ReplyKeyboardMarkup([['Запад', 'Восток'], ['КХЛ','ЦСКА']])
    context.bot.send_message(chat_id=update.effective_chat.id,
    text="I'm a bot, please talk to me!", reply_markup=my_keyboard)

def show_west_conf(update, context):
    cur.execute('select value from description where key="west_conf"')
    text_msg = cur.fetchone()
    west_keyboard = ReplyKeyboardMarkup(
        [['Дивизион\nБоброва', 'Дивизион\nТарасова'], ['КХЛ','ЦСКА']])
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text=text_msg[0],
                            reply_markup=west_keyboard)


def show_east_conf(update, context):
    cur.execute('select value from description where key="west_conf"')
    text_msg = cur.fetchone()
    west_keyboard = ReplyKeyboardMarkup(
        [['Дивизион\nХарламова', 'Дивизион\nЧернышева'], ['КХЛ','ЦСКА']])
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text=text_msg[0],
                            reply_markup=west_keyboard)

viewing_conf = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Запад)$'), show_division)
    ],
    states={'division': []},
    fallbacks=[]
)


dp.add_handler(CommandHandler('start', start))
# dp.add_handler(MessageHandler(Filters.regex('^(Запад)$'), show_west_conf))
dp.add_handler(MessageHandler(Filters.regex('^(Восток)$'), show_east_conf))
dp.add_handler(viewing_conf)

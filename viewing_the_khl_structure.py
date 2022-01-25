from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def show_division(update, context):
    update.message.reply_text(
        'Выберите конференцию, нажав соотвествующую кнопку.',
        reply_markup=ReplyKeyboardMarkup(
        [['Дивизион\nХарламова', 'Дивизион\nЧернышева'], ['КХЛ','ЦСКА']])
    )
    return 'division'

def show_teams(update, context):
    update.message.reply_text(
        'Выберите дивизион, нажав соотвествующую кнопку.',
        reply_markup=ReplyKeyboardMarkup(
        [['ЦСКА\nМосква', 'Локомотив\nЯрославль', 'Северсталь\nЧереповец'],
        ['Динамо\nМосква','Динамо\nРига','Динамо\nМинск',]])
    )
    return 'name'
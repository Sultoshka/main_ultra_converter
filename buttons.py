from telebot import types

def choice():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    eur = types.KeyboardButton('EUR')
    usd = types.KeyboardButton('USD')
    kb.add(eur, usd)
    return kb

import telebot
import buttons
import requests

bot = telebot.TeleBot('7183299123:AAFBK2eo-PPMp9h_cpZTjFgarsNgHi8ETR8')

url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
print(requests.get(url).json()[0])

@bot.message_handler(commands=['start'])
def start(message):
     user_id = message.from_user.id
     bot.send_message(user_id, f'Салам Брат!',
                      reply_markup=buttons.choice())
     bot.register_next_step_handler(message, currancy)


@bot.message_handler(content_types=['text'])
def currancy(message):
    user_id = message.from_user.id
    if message.text.lower() == 'usd':
        bot.send_message(user_id, 'Введите количество в сумах (UZS)')
        bot.register_next_step_handler(message, usd_convert)
    elif message.text.lower() == 'eur':
        bot.send_message(user_id, 'Введите количество в сумах (UZS)')
        bot.register_next_step_handler(message, eur_convert)
    elif message.text.lower() == 'rub':
        bot.send_message(user_id, 'Введите количество в сумах (UZS)')
        bot.register_next_step_handler(message, rub_convert)
    else:
        bot.send_message(user_id, 'Ошыбка в данных!!!')
        bot.register_next_step_handler(message, currancy)



def usd_convert(message):
    user_id = message.from_user.id
    if message.text.isnumeric():
        uzs = int(message.text)
        usd_rate = float(requests.get(url).json()[0]['Rate'])
        bot.send_message(user_id, uzs/usd_rate)
        bot.register_next_step_handler(message, currancy)
    else:
        bot.send_message(user_id, 'Пишите толко числа!')
        bot.register_next_step_handler(message, usd_convert)


def eur_convert(message):
    user_id = message.from_user.id
    if message.text.isnumeric():
        uzs = int(message.text)
        eur_rate = float(requests.get(url).json()[0]['Rate'])
        bot.send_message(user_id, uzs/eur_rate)
        bot.register_next_step_handler(message, currancy)
    else:
        bot.send_message(user_id, 'Пишите толко числа!')
        bot.register_next_step_handler(message, eur_convert)


def rub_convert(message):
    user_id = message.from_user.id
    if message.text.isnumeric():
        uzs = int(message.text)
        rub_rate = float(requests.get(url).json()[0]['Rate'])
        bot.send_message(user_id, uzs/rub_rate)
        bot.register_next_step_handler(message, currancy)
    else:
        bot.send_message(user_id, 'Пишите толко числа!')
        bot.register_next_step_handler(message, rub_convert)

    bot.polling()


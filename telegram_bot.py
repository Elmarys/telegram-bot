import telebot
from utils import ConvertionError, CriptoConverter
from config import TOKEN, keys


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = 'Чтобы начать работу, введите текст в следующем формате:\n' \
           '<наименование котируемой валюты> <наименование базовой валюты> <сумма в котируемой валюте>\n' \
           'Показать список доступных валют: /currencies'
    bot.reply_to(message, text)


# Выводит список доступных валют
@bot.message_handler(commands=['currencies'])
def currencies(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


# Конвертер
@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values = message.text.lower().split(' ')
        if len(values) != 3:
            raise ConvertionError('Введено некорректное количество параметров!')

        base, quote, amount = values
        res = CriptoConverter.convert(quote, base, amount)
        res = '{:,}'.format(res).replace(',', ' ') # форматируем результат, отделяя разряды
    except ConvertionError as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {keys[base]} в {keys[quote]} - {res}'
        bot.send_message(message.chat.id, text)
        print(message.chat.first_name)


bot.polling(none_stop=True)



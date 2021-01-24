import telebot
import json
import requests


TOKEN = '1563086294:AAEJ38N5WrYyl6xC8JzVTMuw3Z3Bdc2dRQA'

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар':'USD',
    'евро':'EUR',
    'биткоин':'BTC'
}

# Обрабатываются все сообщения содержащие команды '/start' or '/help'.
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
        text = '\n'.join((text,key))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text'])
def currencies(message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    global_base = json.loads(r.content)[keys[base]]
    res = global_base * int(amount)
    print(type(global_base))
    text = f'Цена {amount} {keys[quote]} в {keys[base]} - {res}'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
import telebot

TOKEN = '1563086294:AAEJ38N5WrYyl6xC8JzVTMuw3Z3Bdc2dRQA'

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар США':'USD',
    'евро':'EUR',
    'биткоин':'BTC'
}

# Обрабатываются все сообщения содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = 'Чтобы начать работу, введите текст в следующем формате:\n' \
           '<наименование базовой валюты> <в какую валюту перевести> <сумма в базовой валюте>\n' \
           'Показать список доступных валют: /currencies'
    bot.reply_to(message, text)

# Выводит список доступных валют
@bot.message_handler(commands=['currencies'])
def currencies(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key))
    bot.reply_to(message, text)

bot.polling(none_stop=True)
import os
import datetime
import telebot
import requests

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

def money_course():
    privat_api_url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    response = requests.get(privat_api_url)
    course_list = response.json()
    course_EUR_str = 'You can buy EUR by: ' + course_list[0]['buy'] + ' and sell it: ' + course_list[0]['sale']
    course_USD_str = 'You can buy USD by: ' + course_list[1]['buy'] + ' and sell it: ' + course_list[1]['sale']
    return course_EUR_str + '\n' + course_USD_str

@bot.message_handler(commands=['start', 'hello', 'day', 'money_course'])
def send_welcome(message):
    if message.text == '/day':
        bot.reply_to(message, datetime.date.today())
    elif message.text == '/money_course':
        bot.reply_to(message, money_course())
    else:
        bot.reply_to(message,'Hello')

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
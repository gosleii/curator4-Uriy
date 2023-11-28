import telebot

bot = telebot.TeleBot('6831676252:AAHziZ06kPFmtMT_EFcC5pQpJB_3VDLJ6tw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, я BANANA! Как тебя зовут?')


@bot.message_handler(commands=['banana'])
def main(message):
    bot.send_message(message.chat.id, 'You have a big BANANA! ')


@bot.message_handler(commands=['Egor'])
def main(message):
    bot.send_message(message.chat.id, 'You do not have a BANANA!')


@bot.message_handler(commands=['game'])
def main(message):
    bot.send_message(message.chat.id, 'Brawl stars is the best!')


bot.infinity_polling()



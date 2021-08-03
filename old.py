import telebot

bot = telebot.TeleBot("1928658861:AAGJQ4zGVXGAvWF4-l8zT9jAz5imOQSmz8A")

@bot.message_handler(commands=['start'])
def send_welcome(message): 
	bot.reply_to( message, "Como vai você?" )
@bot.message_handler(commands=['entra'])
def send(abc):
  bot.reply_to( abc, "ooaaaaaaaaaa" )
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

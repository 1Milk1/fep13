import config
import telebot

bot = telebot.TeleBot(config.token)
Chat_id = -1001489037561
@bot.message_handler(commands=['everyone'])
def getlist(message):
	admins = "" 
	for admin in bot.get_chat_administrators(message.chat.id):
		if admin.user.username == None or admin.user.id == 459476916 or admin.user.id == 309757771 or admin.user.is_bot == True :
			continue
		admins= admins+ ' @'+admin.user.username
	bot.send_message(message.chat.id, admins)
    

if __name__ == '__main__':
     bot.infinity_polling()

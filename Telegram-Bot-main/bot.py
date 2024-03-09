#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'token'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Написать мне в личку")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привет тебе от белки, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/Ilya-QA/CV.git')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/Fraizer163')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods

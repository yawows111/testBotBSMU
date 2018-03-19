
import telebot

bot = telebot.TeleBot('256863519:AAF9kKEoSBjo2DL6i51-VyJImA0_1ZQII4s') #объект бот

@bot.message_handler(commands=['start','help'])
def handle_start(message):

    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Меню')
    user_markup.row('Информация о Боте.')


    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)
bot.polling(none_stop=True)  # обработка функций
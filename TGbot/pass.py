

import telebot
import configure
from telebot import types
import emoji

bot = telebot.TeleBot(configure.config['token'])


@bot.message_handler(commands=['start'])
def get_user_info(message):
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_parent = types.KeyboardButton(text='Я родитель')
        item_puple = types.KeyboardButton(text='Я ученик')

        markup_reply.add(item_parent, item_puple)
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.username}, чем я могу вам помочь? Чтобы вернуться к началу нажмите /start', reply_markup=markup_reply)

@bot.message_handler(content_types=['text'])
def phone(message):
    if(message.text == "Я родитель"):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_phone = types.KeyboardButton("Отправить свой номер телефона" + emoji.emojize(":mobile_phone_with_arrow:"), request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(message.chat.id, 'Отправьте свой номер телефона, чтобы подтвердить, что вы являетесь родителем, чтобы вернуться к началу нажмите /start', reply_markup=keyboard)






bot.polling(none_stop=True, interval=0)



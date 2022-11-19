# @bot.callback_query_handler(func=lambda call: True)
# def answer(call):
#     if call.data == 'yes':
#         markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item_username = types.InlineKeyboardButton('Укажите ФИО ученика')
#         item_class = types.InlineKeyboardButton('Укажите класс, в котором учится ученик')
#
#         markup_reply.add(item_username, item_class)
#         bot.send_message(call.message.chat.id, 'Заполните информационные окна',
#                          reply_markup=markup_reply
#                          )
#
#     elif call.data == 'no_puple':
#         pass
#     bot.answer_callback_query(callback_query_id=call.id)


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == 'Укажите ФИО ученика':
#         bot.send_message(message.from_username.id, f'ID: {message.from_user.id}')
#     elif message.text == 'Укажите класс, в котором учится ученик':
#         bot.send_message(message.from_username.id, f'ID: {message.from_user.first_name} {message.from_user.last_name}')
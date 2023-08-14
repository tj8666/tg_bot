#TG_Bot2
import telebot
from telebot import types
import buttons

# bot = telebot.TeleBot('5899210772:AAFYWIzpfutI2obBL2UevixJOVS2OUyNv44')
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     text = 'Welocome to this bot'
#     global user_id
#     user_id = message.from_user.id
#     bot.send_message(user_id, text, reply_markup=buttons.menu_kb())

@bot.message_handler(content_types=['text'])
def text_message(message):
    global user_name
    user_name = message.text
    if user_name =='Заказать Услугу':
        bot.send_message(user_id, 'отправьте свое имя', reply_markup=types.ReplyKeyboardRemove())
        # Переход на этап получения имени
        bot.register_next_step_handler(message, get_name)
def get_name(message):
    user_name=message.text
    bot.send_message(user_id, 'good now get your phone number',reply_markup=buttons.num_kb())
    # Переход на этап получения номера
    bot.register_next_step_handler(message, get_number, user_name)
def get_number(message, user_name):
    user_number = message.contact.phone_number
    # Если пользователь отправил номер по кнопке
    if message.contact:
        bot.send_message(user_id, 'What you want to do?', reply_markup=types.ReplyKeyboardRemove())
        #  Переход на этап получения услуги
        bot.register_next_step_handler(message, get_service, get_number, user_name)
    else:
        bot.send_message(user_id, 'Send phone number by botton!')
        # отправляем пользователя обратно
        bot.register_next_step_handler(message, get_number)
def get_service(message, user_name, user_number):
     user_service = message.text
     bot.send_message(user_id, 'How long? ')
     # Перекидываем на этап получения срока
     bot.register_next_step_handler(message, get_deadline, get_number, user_name, user_service)
def get_deadline(message, user_name, user_number, user_service):
    user_deadline = message.text
    bot.send_message(-809697691, f'New order name: {user_name}\n'
                                 f'number{user_number}\n'
                                 f'Service: {user_service}\n'
                                 f'deadline:{user_deadline}')
    bot.send_message(user_id, 'your order accepted, wait for a call, wanna made other order?')
    bot.register_next_step_handler(message, get_service)




bot.polling(non_stop=True)
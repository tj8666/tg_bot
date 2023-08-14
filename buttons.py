from telebot import types
def menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    order_button = types.KeyboardButton('Заказать Услугу')
    kb.add(order_button)
    return kb
def num_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    num_button = types.KeyboardButton('Write phone number', request_contact=True)
    kb.add(num_button)
    return kb
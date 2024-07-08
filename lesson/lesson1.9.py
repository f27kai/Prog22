import telebot
from telebot import types

bot = telebot.TeleBot("7404763837:AAHu_j0B63o969Sycb1U0R22QYB-CA2x-QA")

@bot.message_handler(commands=["start"])
def main(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("Информация")
    btn2 = types.KeyboardButton("Кыргызстан")
    btn3 = types.KeyboardButton("Кыргызстандын желеги")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Welcome to my bot", reply_markup=markup)


@bot.message_handler(commands=['help'])
def info(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Футбол", url='https://www.youtube.com/watch?v=P58VlYO0Le8')
    markup.add(btn1)

    bot.send_message(message.chat.id, "Футбол", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_info(message):
    if message.text == 'Информация':
        bot.send_message(message.chat.id, "Живо́тные — традиционно выделяемая категория организмов, в настоящее время рассматриваемая в качестве биологического царства. Животные являются основным объектом изучения зоологии. Животные относятся к эукариотам. Классическими признаками животных считаются: гетеротрофность и способность активно передвигаться.")
    elif message.text == 'Кыргызстан':
        bot.send_message(message.chat.id, "Кыргызста́н, или Кирги́зия, официально — Кыргы́зская Респу́блика, — государство в Центральной Азии, расположенное в западной и центральной части горной системы Тянь-Шань и на Памиро-Алае. На севере граничит с Казахстаном, на западе — с Узбекистаном, на юго-западе — с Таджикистаном, на востоке и юго-востоке — с Китаем.")
    elif message.text == 'Кыргызстандын желеги':
        bot.send_message(message.chat.id, "Флаг — полотнище правильной геометрической формы, имеющее особую расцветку и определённое соотношение сторон. Знамя — это единичное изделие, тогда как флаг — массового производства. Государственный флаг является одним из государственных символов.")
    elif message.text == "Hello":
        bot.send_message(message.chat.id, "Salam")
    elif message.text == "Атын ким?":
        bot.send_message(message.chat.id, "Менин атым Телебот")
    elif message.text == "Мен айтини билем":
        bot.send_message(message.chat.id, "Мен дагы айтини билем")
    elif message.text == "Кунфу Панда":
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Кунфу Панда", url='https://www.kinopoisk.ru/film/5078842/?utm_referrer=www.google.com')
        markup.add(btn)
        bot.send_message(message.chat.id, "Кунфу Панда", reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, "Your are photo so so beautiful")


bot.polling(none_stop=True)
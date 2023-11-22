from django.core.management.base import BaseCommand
import telebot 
from telebot import types
from myapp.models import Eat
bot = telebot.TeleBot('6617766852:AAHDZB30KZLYd-73Apub77Q5jiLkuMJa6RI')

orders = {}# Словарь для хранения текущих заказов пользователей

#  Если старт написали на русском
@bot.message_handler(commands=['start'])
def handle_start(message):

    welcome_message = f"Привет,{message.from_user.first_name}! Закажи похавать!"
    bot.send_message(message.chat.id, welcome_message)
    menu(message)
    
# Обработка текста 'Помощь'
@bot.message_handler(commands=['help'])
def help(message):
    help_message = "Если у вас возникли сложности или у вас есть вопросы, вы можете обратиться к нашему специалисту в телеграме: @Helper_Vanya. Он свяжется с вами в ближайшее время, чтобы помочь решить вашу проблему. Спасибо, что выбрали нашего бота для заказа еды и напитков на футбольном стадионе!"
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['eats'])
def eats(message):
    eats = Eat.objects.all()
    for eat in eats:
        bot.send_message(message.chat.id, eat.name)

# Меню
def menu(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    eats = Eat.objects.all()

    for eat in eats:
        button_text = f"{eat.name}"
        button = types.InlineKeyboardButton(text=button_text, callback_data=f"eat_{eat.id}")
        keyboard.add(button)
    
    bot.send_message(message.chat.id, 'Вот все что у нас есть:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data.startswith('eat_'):
        eat_id = int(call.data.split('_')[1])

        selected_eat = Eat.objects.get(id=eat_id)
        response_text = f"Вы выбрали продукт: {selected_eat.name}"
        bot.send_message(call.message.chat.id, response_text)
        

@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')


bot.polling(none_stop=True)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

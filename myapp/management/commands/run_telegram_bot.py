from django.core.management.base import BaseCommand
import telebot 
from telebot import types
from myapp.models import Eat
bot = telebot.TeleBot('6617766852:AAHDZB30KZLYd-73Apub77Q5jiLkuMJa6RI')

@bot.message_handler(commands=['start'])
def handle_start(message):

    welcome_message = f"Привет,{message.from_user.first_name}! Закажи похавать!"
    bot.send_message(message.chat.id, welcome_message)

@bot.message_handler(commands=['help'])
def help(message):
    help_message = "Если у вас возникли сложности или у вас есть вопросы, вы можете обратиться к нашему специалисту в телеграме: @Helper_Vanya. Он свяжется с вами в ближайшее время, чтобы помочь решить вашу проблему. Спасибо, что выбрали нашего бота для заказа еды и напитков на футбольном стадионе!"
    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands=['eats'])
def eats(message):
    eats = Eat.objects.all()
    for eat in eats:
        bot.send_message(message.chat.id, eat.name)
        
@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')


bot.polling(none_stop=True)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

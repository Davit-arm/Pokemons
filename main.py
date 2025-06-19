import telebot 
from config import token

from logic import Pokemon, Wizard, Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = (1, 5)
        if chance == 1 or 2 or 3:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 4:
            pokemon = Wizard(message.from_user.username)
        elif chance ==5:
            pokemon = Fighter(message.from_user.usernamer)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.ab())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attacks(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            yourpok = Pokemon.pokemons[message.from_user.username]
            res = yourpok.attack(enemy)
            bot.send_message(message.chat.id, res)

        else:
            bot.send_message(message.chat.id, 'You can only fight with pokemons')
    else:
        bot.send_message(message.chat.id, "You have to reply to a certain person's message to attack")


bot.infinity_polling(none_stop=True)


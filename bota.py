
from time import sleep
from random import randint
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot=ChatBot('Zacker')
bot.set_trainer(ListTrainer)
def respond(msg):
    return bot.get_response(msg)
#bot.train("chatterbot.corpus.english")


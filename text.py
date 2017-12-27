# coding=utf-8

from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.chinese")

# Get a response to an input statement
chatbot.get_response("为什么两个鼻孔?")
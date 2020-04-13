from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('cérebro')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the portuguese corpus
trainer.train("chatterbot.corpus.portuguese")

while True:
    request = input("Você: ")
    response = chatbot.get_response(request)
    print("bot: %s" % response)

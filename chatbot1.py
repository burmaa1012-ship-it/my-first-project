from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Chatbot үүсгэх
chatbot = ChatBot('MyBot')

# Хялбар датагаар сургах
trainer = ListTrainer(chatbot)
trainer.train(["Сайн уу","Сайн байна уу", "Юу байна?","Зүгээрээ баярлалаа"])

# Харилцан яриа
while True:
    question = input("Та:") 
    response = chatbot.get_response(question)
    print("AI:", response)
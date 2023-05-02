from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


bot = ChatBot('chatbot', read_only=False, 
              logic_adapters=[
                  { 
                      'import_path':'chatterbot.logic.BestMatch'
                      
                      }])

list_to_train = [
    "hi",
    "hi,there",
    "what is your name?",
    "i am jsut a chatbot"
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
chatterbotCorpusTrainer .train('chatterbot.corpus.english')


def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("list1")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)



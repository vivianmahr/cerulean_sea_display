from django.shortcuts import render
from django.http import HttpResponse
import requests

import en_core_web_sm
nlp= en_core_web_sm.load()

from .models import Greeting

# Create your views here.
def index(request):
    
    r = requests.get('http://httpbin.org/status/418')
    print(nlp)
    print(r.text)
    return HttpResponse('<pre>' + r.text + 'loaded!</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


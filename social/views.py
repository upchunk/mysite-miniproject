from django.shortcuts import render
import urllib.request
import json
from random import randint
from .models import *


# Create your views here.

def index(request):
    request.method == 'POST'
    # retrieve imformation from weather api = https://weatherapi.com/api-explorer
    source = urllib.request.urlopen('http://api.weatherapi.com/v1/current.json?key=36b8d07f77ff471e80a60553220903&q=Surabaya&aqi=no').read()
    # convert  json file into python dectionary
    list_of_data =json.loads(source)

    data ={
            'temp':str(list_of_data["current"]['temp_c']),
            'description':str(list_of_data["current"]['condition']['text']),
            'icon':list_of_data["current"]['condition']['icon'],
            'city':str(list_of_data['location']['name'])
        }
    return render(request,'social/index.html',data)

def home(request):
    accounts = Account.objects.all()
    posts = Post.objects.all()
    context =  {'accounts':accounts,
                'posts':posts}
    return render (request, 'social/home.html', context)

def user(request):
    context = {}
    return render (request, 'social/user.html', context)
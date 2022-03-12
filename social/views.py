from django.shortcuts import render
import urllib.request
import json
from .models import *


# Create your views here.

def login(request):
    request.method == 'POST'
    # retrieve imformation from weather api = https://weatherapi.com/api-explorer
    source = urllib.request.urlopen('http://api.weatherapi.com/v1/current.json?key=36b8d07f77ff471e80a60553220903&q=Surabaya&aqi=no').read()
    # convert  json file into python dectionary
    list_of_data =json.loads(source)

    data ={
            'country_code':str(list_of_data['location']['country']),
            'temp':str(list_of_data["current"]['temp_c']),
            'pressure':str(list_of_data["current"]["pressure_mb"]),
            'humidity':str(list_of_data["current"]['humidity']),
            'description':str(list_of_data["current"]['condition']['text']),
            'icon':list_of_data["current"]['condition']['icon'],
            'city':str(list_of_data['location']['name'])
        }
    return render(request,'social/login.html',data)

def home(request):
    account = Account.objects.all()
    posts = Post.objects.all()
    context = {'account':account,'posts':posts}
    return render (request, 'social/home.html', context)

def user(request):
    context = {}
    return render (request, 'social/user.html', context)

def checkout(request):
    context = {}
    return render (request, 'social/checkout.html', context)

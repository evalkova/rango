from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")

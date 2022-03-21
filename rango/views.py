from  django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="rango/about/">"Rango says this is the about page"</a>')


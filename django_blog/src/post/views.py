from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    print(request.scheme)
    print(request.path)
    print(request.encoding)
    return HttpResponse ('<h1>Hello World!</h1>')

def about(request):
    print('http://127.0.0.1:8000'+request.get_full_path())
    return HttpResponse ('<a href="#"> About page!</a>') 

def contacts(request):
    return HttpResponse ('<h2>Contacts page</h2>') 

def ggg(request):
    return HttpResponse ('<h2> GGG page</h2>') 

def arсhive(request):
    return HttpResponse ('number page') 


def home(request):
    return HttpResponse('<h1>HOME</h1>')
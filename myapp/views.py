from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Hello World!')


def profile(request):
    return HttpResponse('This is the profile page')


def dashboard(request):
    return HttpResponse('This is the dashboard page')


data = {
    "title": "Welcome to Django Templates Contex Feature",
    "word": "Django Templates Contex Feature",
    "sentence": "This is a simple Django Template"
}


def about(request):
    return render(request, 'about.html', data)

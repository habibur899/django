from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta


# Create your views here.
def home(request):
    return HttpResponse('Hello World!')


def profile(request):
    data = {
        "user": {"is_authenticated": True, "username": "Habibur"},
        "title": "The quick brown fox jumps over the lazy dog",
        "products": [{"name": "Samsung Galaxy S21", "price": 75000},
                     {"name": "Apple iPhone 14 Pro Max", "price": 80000},
                     {"name": "Samsung Galaxy S22", "price": 90000},
                     {"name": "Apple iPhone 14 Pro", "price": 100000},
                     {"name": "Samsung Galaxy S23", "price": 110000},
                     {"name": "Apple iPhone 15 Pro", "price": 120000},
                     {"name": "Samsung Galaxy S24", "price": 130000},
                     {"name": "Apple iPhone 15 Pro Max", "price": 140000},
                     ]
    }

    return render(request, 'profile.html', data)


def dashboard(request):
    return HttpResponse('This is the dashboard page')


def about(request):
    data = {
        "title": "The quick brown fox jumps over the lazy dog",
        "name": "habibur",
        "word": "Django Templates Contex Feature",
        "sentence": "This is a simple Django Template",
        "number": "1234567890",
        "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "my_dict": {"name": "habibur", "age": 25, "city": "Lahore"},
        "my_html": "<h1><i>Hello World!</i></h1>",
        "my_date": datetime.now() - timedelta(days=365),
        "my_string": "alert('hello');",
        "my_var": None,
        "is_bangladeshi": True,

        "my_dict_list": [{"name": "habibur", "age": 15, "city": "Dhaka"},
                         {"name": "ali", "age": 25, "city": "Khulna"},
                         {"name": "hassan", "age": 35, "city": "Jessore"},
                         ]
    }
    context = data.copy()
    context["current_date"] = datetime.now()
    return render(request, 'about.html', context)

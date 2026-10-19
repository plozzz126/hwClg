from django.shortcuts import render
import requests
## рандом пррст что бы фотки рандммные былм
import random

def index(request):
    users = [
        {
            "id": 1,
            "name": "I",
            "age": 18,
        },
        {
            "id": 2,
            "name": "chak",
            "age": 76,
        },
    ]

    context = {
        "users": users
    }

    return render (request, 'app/index.html', context)


def photo(request):
    photos = []

    API = "https://jsonplaceholder.typicode.com/photos"    
    response = requests.get(API)
    photos = random.sample(response.json(), 10)
    
    context = {
        "photos": photos,
    }

    return render (request, 'app/randomphoto.html', context)

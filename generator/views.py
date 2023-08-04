from django.shortcuts import render

import random


def home(request):
    return render(request, 'generator/home.html', {'password': 12345})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html',{'password': thepassword})


def description(request):
    info_text = "Welcome to the Password Generator app!" \
                "for your account"
    
    options = [
        "Include uppercase letters (A-Z)",
        "Include special characters (!@#$%^&*())",
        "Include numbers (0-9)"
    ]
    return render(request, 'generator/description.html', {'info_text': info_text, 'options': options})

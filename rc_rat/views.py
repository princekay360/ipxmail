# chat/views.py
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "rc_home.html", {"room_name": room_name})
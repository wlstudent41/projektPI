from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def hello(request):
    return HttpResponse("Witaj w django!")

def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

def hello_template (request, name):
    return render(request, "witaj/hello.html", {"name":name})

def showtime(request):
    now = datetime.now()
    return render(request, "witaj/time.html", {"current_time": now})
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import models

# Create your views here.
def LandingPage(request):
    return render(request, "main.html", {})

def ReturnMusic(request):
    musics = list(models.Music.objects.all().values())
    return JsonResponse(musics, safe=False)
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import models

# Create your views here.
def LandingPage(request):
    return render(request, "main.html", {})

def ReturnMusic(request):
    if request.method != "GET":
        return

    musicObjects = models.Music.objects.all()
    print(musicObjects)

    filterTitle = request.GET.get("title", "").strip()
    if filterTitle != "":
        musicObjects = musicObjects.filter(title__icontains=filterTitle)
    print(musicObjects)

    filterAlbum = request.GET.get("album", "").strip()
    if filterAlbum != "":
        musicObjects = musicObjects.filter(album__icontains=filterAlbum)
    print(musicObjects)

    filterArtist = request.GET.get("artist", "").strip()
    if filterArtist != "":
        musicObjects = musicObjects.filter(artist__icontains=filterArtist)
    print(musicObjects)

    musics = list(musicObjects.values())
    print(musics)
    
    return JsonResponse(musics, safe=False)
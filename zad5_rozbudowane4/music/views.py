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


    # DODANe order_by dla api
    orderAsc = request.GET.get("order_asc", "").strip()
    if orderAsc != "":
        musicObjects = musicObjects.order_by("title")
    
    orderDesc = request.GET.get("order_desc", "").strip()
    if orderDesc != "":
        musicObjects = musicObjects.order_by("-title")

    # dodane ograniczenie do wybranej liczby zwracanych rekordow, z obsluga bledow
    limitTo = request.GET.get("limit", "").strip()
    if limitTo != "":
        try:
            limitTo = int(limitTo)
            musicObjects = musicObjects[:limitTo]
        except:
            print("Cos poszlo nie tak przy braniu limit rekordow")
        

    musics = list(musicObjects.values())
    print(musics)
    
    return JsonResponse(musics, safe=False)
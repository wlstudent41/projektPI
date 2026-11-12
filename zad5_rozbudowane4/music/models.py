from django.db import models

# Create your models here.
class Music(models.Model):
    # nie dodaje unikalnych kluczy ze wzgledu na mozliwosc powtorzenia sie tytulow i albumow artysty gdy np robi remiksy albo anniversary i nie zmienia tytulow, co sie zdarzylo naprawde
    title=models.CharField(max_length=100)
    album=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    plays=models.IntegerField()
    released=models.DateField()

    #nowe rozbudowane dwa pola pasujace do tematu aplikacji
    rating=models.IntegerField(default=3)
    wishlists=models.IntegerField(default=1000)

    # makemigrations i migrate bylo zrobione bez bledu
    # sa domyslne wartosci default do migracji 

    # czytelna reprezentacja obiektu string
    def __str__(self):
        return "\""+self.title+"\", " + self.album + ", by: " + self.artist
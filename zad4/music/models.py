from django.db import models

# Create your models here.
class Music(models.Model):
    title=models.CharField(max_length=100)
    album=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    plays=models.IntegerField()
    released=models.DateField()

    def __str__(self):
        return "\""+self.title+"\", " + self.album + ", by: " + self.artist
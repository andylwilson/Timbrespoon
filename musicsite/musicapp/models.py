from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    genrename=models.CharField(max_length=255)
    genredescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.genrename

    class Meta:
        db_table='genre'
        verbose_name_plural='genres'

class Album(models.Model):
    albumname=models.CharField(max_length=255)
    genre=models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    artist=models.CharField(max_length=255)
    issueyear=models.SmallIntegerField()
    tracks=models.SmallIntegerField()

    def __str__(self):
        return self.albumname

    class Meta:
        db_table='album'
        verbose_name_plural='albums'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    album=models.ForeignKey(Album, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    rating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table='review'
        verbose_name_plural='reviews'
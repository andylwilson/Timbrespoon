from django.contrib import admin
from .models import Album, Genre, Review

# Register your models here.
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Review)
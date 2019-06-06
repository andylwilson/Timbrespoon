from django import forms
from .models import Album, Genre, Review

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
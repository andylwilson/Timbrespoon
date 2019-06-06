from django.shortcuts import render, get_object_or_404
from .models import Album, Genre, Review
from .forms import AlbumForm, GenreForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'musicapp/index.html')

def getGenres(request):
    genre_list=Genre.objects.all()
    context={'genre_list' : genre_list,}
    return render(request, 'musicapp/genres.html', context=context)

def getAlbums(request):
    album_list=Album.objects.all()
    return render(request,'musicapp/albums.html',{'album_list' : album_list})

def albumDetail(request, id):
    album=get_object_or_404(Album, pk=id)
    context={'album' : album,}
    return render (request, 'musicapp/albumdetail.html', context=context)

@login_required
def newAlbum(request):
     form=AlbumForm
     if request.method=='POST':
          form=AlbumForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=AlbumForm()
     else:
          form=AlbumForm()
     return render(request, 'musicapp/newalbum.html', {'form': form})

@login_required
def newGenre(request):
     form=GenreForm
     if request.method=='POST':
          form=GenreForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=GenreForm()
     else:
          form=GenreForm()
     return render(request, 'musicapp/newgenre.html', {'form': form})

@login_required
def newreview(request):
     form=ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm()
     return render(request, 'musicapp/newreview.html', {'form': form})

def loginMessage(request):
     return render(request,'musicapp/loginmessage.html')

def logoutMessage(request):
     return render(request, 'musicapp/logoutmessage.html')
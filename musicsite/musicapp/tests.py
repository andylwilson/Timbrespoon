from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Album, Genre, Review
import datetime
from .forms import AlbumForm, GenreForm, ReviewForm

# Create your tests here.

# Tests for models
class GenreTest(TestCase):
    def test_string(self):
        genre=Genre(genrename='Electronic')
        self.assertEqual(str(genre), genre.genrename)

    def test_table(self):
        self.assertEqual(str(Genre._meta.db_table), 'genre')


class AlbumTest(TestCase):
    def setUp(self):
        self.genre=Genre(genrename='Electronic')
        self.album=Album(
            albumname='Crystal Castles',
            genre=self.genre,
            artist='Crystal Castles',
            issueyear=2008,
            tracks=16,)

    def test_string(self):
        self.assertEqual(str(self.album),self.album.albumname)
    
    def test_genre(self):
        self.assertEqual(str(self.album.genre), 'Electronic')

    def test_artist(self):
        self.assertEqual(str(self.album.artist),'Crystal Castles')

    def test_issueyear(self):
        self.assertEqual(self.album.issueyear,2008)

    def test_tracks(self):
        self.assertEqual(self.album.tracks,16)
    
# Tests for views

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetAlbumsTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='testUser')
        self.genre=Genre.objects.create(genrename='Electronic')
        self.album=Album.objects.create(
            albumname='Crystal Castles',
            genre=self.genre,
            user=self.user,
            artist='Crystal Castles',
            issueyear=2008,
            tracks=16,)

    def test_album_detail_success(self):
        response=self.client.get(reverse('albumdetail', args=(self.album.id,)))
        self.assertEqual(response.status_code, 200)

# Tests for forms

class AlbumFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='testUser', password='P@ssw0rd1')
        self.genre=Genre.objects.create(genrename='Electronic')

    def test_AlbumForm(self):
        data={
            'albumname' : 'Crystal Castles',
            'genre' : self.genre,
            'user' : self.user,
            'artist' : 'Crystal Castles',
            'issueyear' : 2008,
            'tracks' : 16
        }
        form = AlbumForm(data=data)
        self.assertTrue(form.is_valid)

    def test_AlbumFormInvalid(self):
        data={
            'albumname' : '',
            'genre' : self.genre,
            'user' : self.user,
            'artist' : 'Crystal Castles',
            'issueyear' : 2008,
            'tracks' : 16
        }
        form = AlbumForm(data=data)
        self.assertFalse(form.is_valid())
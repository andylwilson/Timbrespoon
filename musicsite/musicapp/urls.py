from django.urls import path
from . import views

# project url directs to this, which directs to the proper view
urlpatterns=[
    path('', views.index, name='index'),
    path('getGenres/', views.getGenres, name='genres'),
    path('getAlbums/', views.getAlbums, name='albums'),
    path('albumDetail/<int:id>', views.albumDetail, name='albumdetail'),
    path('newAlbum/', views.newAlbum, name='newalbum'),
    path('newreview/', views.newreview, name='newreview'),
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]
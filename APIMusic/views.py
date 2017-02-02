from APIMusic.models import *
from APIMusic.serializers import *
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Albums.objects.all()
	serializer_class = AlbumSerializer

class ArtistViewSet(viewsets.ModelViewSet):
	queryset = Artists.objects.all()
	serializer_class = ArtistSerializer

class SongViewSet(viewsets.ModelViewSet):
	queryset = Songs.objects.all()
	serializer_class = SongSerializer

class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genres.objects.all()
	serializer_class = GenreSerializer
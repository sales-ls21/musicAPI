from rest_framework import serializers
from APIMusic.models import *


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Albums 
		fields = '__all__'

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Artists 
		fields = '__all__'

class SongSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Songs 
		fields = '__all__'

class GenreSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Genres 
		fields = '__all__'




from django.db import models

# Create your models here.
class Genres(models.Model):

	name = models.CharField(max_length=50)

	def __str__(self):
		return '{0}'.format(self.name)

class Artists(models.Model):

	name = models.CharField(max_length=60, blank=False)
	genre = models.ForeignKey(Genres, null=True)
	hometown = models.CharField(max_length=50, blank=False)
	description = models.CharField(max_length=250)

	def __str__(self):
		return '{0}'.format(self.name)
		
class Albums(models.Model):

	title = models.CharField(max_length=50, blank=False, default='')
	artist = models.ForeignKey(Artists, null=True)
	genre = models.ForeignKey(Genres, null=True)
	year_released = models.CharField(max_length=50)

	def __str__(self):
		return '{0}'.format(self.title)

class Songs(models.Model):

	name = models.CharField(max_length=60, blank=False)
	album = models.ForeignKey(Albums, null=True)
	genre = models.ForeignKey(Genres, null=True)
	artist = models.ForeignKey(Artists, null=True)
	year_released = models.CharField(max_length=50)

	def __str__(self):
		return '{0}'.format(self.name)




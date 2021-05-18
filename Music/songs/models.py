import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from Music.settings import MEDIA_ROOT

def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.album_artist.id, filename)

def user_directory_path_song(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return 'user_{0}/{1}'.format(self.song_album.album_artist.id, filename)

# Create your models here.
class Album(models.Model):
	album_name=models.CharField(max_length=100)
	upload=models.DateField(default=timezone.now())
	logo=models.FileField(upload_to="logo")
	genre=models.CharField(max_length=100)
	artist=models.ForeignKey(User,related_name="albums",on_delete=models.CASCADE)

	def __str__(self):
		return self.album_name

	def delete_media(self):
		os.remove(path=MEDIA_ROOT+'/'+str(self.album_logo))

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    song_file = models.FileField(upload_to="song")

    def __str__(self):
        return self.song_name +' '+ str(self.song_album)

    def delete_media(self):
        os.remove(path=MEDIA_ROOT+'/'+str(self.song_file))
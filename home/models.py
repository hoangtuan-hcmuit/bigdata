from django.db import models

# Create your models here.
class Track (models.Model):
    genre = models.CharField(('genre'), max_length=225)
    artist_name = models.CharField(('artist_name'), max_length=225)
    track_name = models.CharField(('track_name'), max_length=225)
    track_id = models.IntegerField(('track_id'), primary_key=True)
    popularity = models.IntegerField(('popularity'))
    acousticness = models.FloatField(('acousticness'))
    danceability = models.FloatField(('danceability'))
    duration_ms	= models.IntegerField(('duration_ms'))
    energy = models.FloatField(('energy'))
    instrumentalness = models.FloatField(('instrumentalness'))
    key	= models.CharField(('key'), max_length=225)
    liveness = models.FloatField(('liveness'))
    loudness = models.FloatField(('loudness'))
    mode = models.CharField(('mode'), max_length=225)
    speechiness = models.FloatField(('speechiness'))
    tempo = models.FloatField(('tempo'))
    time_signature = models.CharField(('time_signature'), max_length=225)
    valence = models.FloatField(('valence'))

class UserTrack (models.Model):
    user_id = models.IntegerField(('user_id'), primary_key=True)
    track_id = models.IntegerField(('track_id'))
    rating = models.IntegerField(('rating'))
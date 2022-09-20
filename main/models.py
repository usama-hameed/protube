from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateField(default=date.today)
    comment_text = models.TextField(max_length=200)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)


class Videos(models.Model):
    title = models.CharField(max_length=225, default='', null=False, unique=True)
    uploaded_date = models.DateField(default=date.today)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)


class Playlist(models.Model):
    name = models.CharField(max_length=225, default='', null=False, unique=True)
    created_date = models.DateField(default=date.today)


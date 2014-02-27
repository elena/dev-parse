from datetime import datetime
from django.db import models
from posts.models import Post


class Podcast(models.Model):

    date = models.DateField()

    def __str__(self):
        return datetime.strptime(self.date, "%y%m%d")


class PostPodcast(models.Model):

    podcast = models.ForeignKey(Podcast)
    post = models.ForeignKey(Post)

    order = models.IntegerField(default=0)

    notes = models.TextField(blank=True)

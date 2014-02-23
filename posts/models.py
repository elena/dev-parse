from django.db import models
from taggit.managers import TaggableManager


class Author(models.Model):

    full_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)


class Ticket(models.Model):

    number = models.CharField(max_length=6)
    description = models.CharField(max_length=256)


class AbstractPost(models.Model):

    title = models.CharField(max_length=256)
    author_original = models.ForeignKey(Author)
    posted_at = models.DateTimeField()
    contents = models.TextField(blank=True)

    class Meta:
        abstract = True


class Post(AbstractPost):

    url = models.CharField(max_length=256)
    views = models.PositiveIntegerField()

    tickets = models.ManyToManyField(Ticket, null=True, blank=True)

    last_checked_at = models.DateTimeField(auto_now=True)

    tags = TaggableManager()


class PostChild(AbstractPost):

    parent = models.ForeignKey(Post)
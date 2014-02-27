from django.contrib import admin

from podcasts.models import Podcast, PostPodcast


class PostPodcastInline(admin.TabularInline):

    model = PostPodcast


class PodcastAdmin(admin.ModelAdmin):

    inlines = [PostPodcastInline]

admin.site.register(Podcast, PodcastAdmin)

from django.contrib import admin
from posts.models import Post, PostChild, Author, Ticket

class PostChildInline(admin.StackedInline):

    model = PostChild


class PostAdmin(admin.ModelAdmin):

    inlines = [PostChildInline]


admin.site.register(Post, PostAdmin)

admin.site.register(Author)

admin.site.register(Ticket)

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'datecreation']
    list_filter = ('author', 'datecreation')


admin.site.register(Post, PostAdmin)

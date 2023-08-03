from django.contrib import admin
from .models import Comments, Post


class PostAdmin(admin.ModelAdmin):
    # fields = ['text', 'title', 'author'] This is for ordering the fields in the model
    search_fields = ['title']
    list_filter = ['author', 'published_date', ]
    list_display = ['author', 'title', 'published_date']


admin.site.register(Post, PostAdmin)
admin.site.register(Comments)




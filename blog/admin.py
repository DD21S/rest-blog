from django.contrib import admin

from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''
    list_display = ('title', 'author')
    list_filter = ('published',)
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)

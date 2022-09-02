from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status','publish')
    list_filter =('created','publish','updated')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    ordering =('status','publish')
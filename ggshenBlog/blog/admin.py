from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Photo, Video, MiniRecord

admin.site.register(Article)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(MiniRecord)

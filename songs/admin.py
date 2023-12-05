from django.contrib import admin
from .models import Song, PlayList

# Register your models here.
admin.site.register(Song)
admin.site.register(PlayList)
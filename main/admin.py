from django.contrib import admin
from .models import Videos, Comments, Playlist
# Register your models here.

admin.site.register(Videos)
admin.site.register(Comments)
admin.site.register(Playlist)

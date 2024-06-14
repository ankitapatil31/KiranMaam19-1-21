from django.contrib import admin
from .models import MitraCoordinatePhotos


# Register your models here.

class adminCoordinatePhotos(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'image']

admin.site.register(MitraCoordinatePhotos, adminCoordinatePhotos)

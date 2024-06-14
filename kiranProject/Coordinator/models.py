from django.db import models

# Create your models here.
from django.db import models


class MitraCoordinatePhotos(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploadimage/Mitra-Coordinator/')


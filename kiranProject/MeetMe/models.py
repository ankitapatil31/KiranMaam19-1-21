from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.

class PersonalInfo(models.Model):
    Titles = models.CharField(max_length=100, null=False)
    date_created = models.DateTimeField(verbose_name="Creation date", auto_now_add=True, null=True)
    image = models.ImageField(upload_to='PersonalImage', default='DefaultBlog.png')
    update_to = models.DateTimeField(auto_now=True)
    content = FroalaField()


class FacultyDevelopment(models.Model):
    Title = models.CharField(max_length=100, null=False)
    Duration = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

    from rest_framework import serializers


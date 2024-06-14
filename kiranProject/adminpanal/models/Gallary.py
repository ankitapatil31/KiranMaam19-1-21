from django.db import models


class category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class AddPhotos(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='uploadimage/photos/')

    @staticmethod
    def get_all_Photos_by_category(category_id):
        if category_id:
            return AddPhotos.objects.filter(category=category_id)
        else:
            return AddPhotos.objects.all()

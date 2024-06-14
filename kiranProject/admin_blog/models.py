from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.

class BlogCaterogy(models.Model):
    Name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.Name


class Blog(models.Model):
    Titles = models.CharField(max_length=100,null=False)
    Category = models.ForeignKey(BlogCaterogy,on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(verbose_name="Creation date", auto_now_add=True, null=True)
    image = models.ImageField(upload_to='BlogImg',default='DefaultBlog.png')
    update_to = models.DateTimeField(auto_now=True)
    content = FroalaField()


class comment(models.Model):
    Comment_id = models.IntegerField(primary_key=True)
    blogid = models.IntegerField(default=0)
    name = models.CharField(max_length=150,default='')
    emailid = models.CharField(max_length=150,default='')
    createdate = models.DateTimeField(verbose_name="Creation date", auto_now_add=True, null=True)
    Comment = models.CharField(max_length=200,default='')


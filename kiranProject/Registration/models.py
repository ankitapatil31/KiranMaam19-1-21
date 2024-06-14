from django.db import models


# Create your models here.
class Registration(models.Model):
    EmailID = models.EmailField(primary_key=True)
    MobileNo = models.IntegerField(blank=True)
    Password = models.CharField( max_length=24)
    ConfirmPassword = models.CharField(max_length=24)




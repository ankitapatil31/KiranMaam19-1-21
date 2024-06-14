from django.db import models


# Create your models here.


class Bookappointment(models.Model):
    Name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    contactNo = models.CharField(max_length=10,default='0000000000')
    Date = models.DateTimeField()
    content = models.TextField()


class Message(models.Model):
    Name = models.CharField(max_length= 100)
    EmailId = models.CharField(max_length=100)
    Message = models.TextField()

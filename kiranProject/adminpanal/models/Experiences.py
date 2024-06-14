from django.db import models
import datetime

class Experiences(models.Model):
    currently_working=models.BooleanField()
    formDate = models.CharField(max_length=20)
    toDate = models.CharField(max_length=20)
    organization_name = models.CharField(max_length=80)
    designation = models.CharField(max_length=80)
    description = models.TextField()

    def convert_DateString_To_Date(self):
        date_obj = datetime.strptime(self, '%d/%m/%y')
        return date_obj

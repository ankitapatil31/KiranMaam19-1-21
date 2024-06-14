from django.contrib import admin
from .models import Bookappointment, Message


# Register your models here.


class AdminMessage(admin.ModelAdmin):
    list_display = ['Name', 'EmailId', 'Message']


class AdminBookAppointment(admin.ModelAdmin):
    list_display = ['Name','email','contactNo','Date','content']


admin.site.register(Message, AdminMessage)
admin.site.register(Bookappointment, AdminBookAppointment)

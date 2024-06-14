from django.contrib import admin
from .models import PersonalInfo,FacultyDevelopment

# Register your models here.


class adminPersonalInfo(admin.ModelAdmin):
    list_display = ['id','Titles','date_created','image','update_to','content']


class adminFacultyDevelopment(admin.ModelAdmin):
    list_display = ['Title','Duration']


admin.site.register(PersonalInfo, adminPersonalInfo)
admin.site.register(FacultyDevelopment, adminFacultyDevelopment)
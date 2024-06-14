from django.contrib import admin
from .models import FileUpload


# Register your models here.

class adminFileUpload(admin.ModelAdmin):
    list_display = ['id','title','pdf']


admin.site.register(FileUpload, adminFileUpload)

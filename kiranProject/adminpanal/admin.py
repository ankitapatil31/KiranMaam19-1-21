from django.contrib import admin
from .models import Skillset, Experiences
from .models.Gallary import AddPhotos, category


# Register your models here.

class adminSkillset(admin.ModelAdmin):
    list_display = ['id','Skill', 'Rateing']


class adminExperience(admin.ModelAdmin):
    list_display = ['id','formDate', 'toDate', 'organization_name', 'designation', 'description', 'currently_working']


class adminAddPhotos(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'image']


class admincategory(admin.ModelAdmin):
    list_display = ['id','category']


admin.site.register(Skillset, adminSkillset)
admin.site.register(Experiences, adminExperience)
admin.site.register(AddPhotos, adminAddPhotos)
admin.site.register(category, admincategory)

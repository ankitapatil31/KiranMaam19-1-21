from django.contrib import admin
from .models import Blog, BlogCaterogy, comment


# Register your models here.
class admin_Blog_create(admin.ModelAdmin):
    list_display = ['id', 'Titles', 'Category', 'date_created','image','update_to','content']


class admin_comment(admin.ModelAdmin):
    list_display = ['Comment_id','blogid','name','emailid','createdate','Comment']


class admin_BlogCaterogy(admin.ModelAdmin):
    list_display = ['id', 'Name']


admin.site.register(Blog,admin_Blog_create)
admin.site.register(BlogCaterogy,admin_BlogCaterogy)
admin.site.register(comment,admin_comment)

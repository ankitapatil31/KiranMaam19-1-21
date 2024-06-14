from django.shortcuts import render
from admin_blog.models import Blog

# Create your views here.

def IndexPage(request):
    context = {'popularblog': Blog.objects.all()[0:4]}
    return render(request, 'Base/indexPage.html' ,context)

from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Blog,comment,BlogCaterogy
from .form import BlogForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def ViewBlog(request):
    context = {'blogs': Blog.objects.all(),'categorys':BlogCaterogy.objects.all()}
    return render(request, 'admin_blog/ViewBlog.html', context)


def ViewFilterByCategory(request):
    print('blogs')
    var = request.POST.getlist('checks[]')
    print(var)
    return render(request,'admin_blog/ViewBlog.html')

def searchblog(request):

    if request.method == 'GET':
        qu = request.GET.get('search')
        lookup=(Q(Titles__icontains = qu) or Q(Category__icontain=qu))
        context = {'blogs': Blog.objects.filter(lookup),'categorys':BlogCaterogy.objects.all()}
        countno = 0
        countno = Blog.objects.filter(lookup).count()
        if countno <= 0:
            messages.info(request, f"No Result Found.")
            context = {'blogs': Blog.objects.all(),'categorys':BlogCaterogy.objects.all()}
    else:
        context = {'blogs': Blog.objects.all(),'categorys':BlogCaterogy.objects.all()}
    print('blogs')
    return render(request, 'admin_blog/ViewBlog.html',context)

def Postcomment(request,blogid):
    try:
        print(blogid)
        if request.method == "POST":
            print(blogid)
            name = request.POST.get('name')
            message = request.POST.get('msg')
            emailid = request.POST.get('email')
            comment_obj = comment.objects.create(
                blogid=blogid,
                name=name, emailid=emailid,
                Comment=message
            )
            print("hii")
    except Exception as e:
        print(e)
    context = {'blogs': Blog.objects.all(), 'categorys': BlogCaterogy.objects.all()}
    return render(request,'admin_blog/ViewBlog.html',context)


def BlogDetails(request, id):
    context = {'blogs': Blog.objects.get(pk=id),'popularblog':Blog.objects.all()[1:4],'comments':comment.objects.filter(blogid=id)}
    return render(request, 'admin_blog/Blog_Details.html', context)


def Create_Blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')

            if form.is_valid():
                content = form.cleaned_data['content']
                Category = form.cleaned_data['Category']

            blog_obj = Blog.objects.create(
                Titles=title, Category=Category,
                content=content, image=image
            )
            print(blog_obj)
            return redirect('/')



    except Exception as e:
        print(e)

    return render(request, 'admin_blog/Blog_panal.html', context)

def ViewSendmail(request):
    try:
        if request.method == 'POST':
            recipient = request.POST.get('Recipient')
            mymessage =  request.POST.get('message')
            send_mail('subject',mymessage,recipient,[settings.EMAIL_HOST_USER],fail_silently=False)
            print("ok")
    except Exception as e:
        print(e)

    context = {'blogs': Blog.objects.all(), 'categorys': BlogCaterogy.objects.all()}
    return render(request, 'admin_blog/ViewBlog.html', context)

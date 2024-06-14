from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.ViewBlog,name='Blog_Page'),
    path('Create_blog/',views.Create_Blog,name='Create_BLog'),
    path('froala_editor/',include('froala_editor.urls')),
    path('BlogDetails<str:id>/',views.BlogDetails,name='Blog_Details'),
    path('search',views.searchblog,name='search'),
    path('comment<str:blogid>',views.Postcomment,name='Add_Comment'),
    path('FilterByCategory',views.ViewFilterByCategory,name='FilterByCategory'),
    path('SendEmail/',views.ViewSendmail,name='SendEmail')
    #path('',)
]
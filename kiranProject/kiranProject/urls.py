"""kiranProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import settings
from froala_editor import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('froala_editor/', include('froala_editor.urls')),
                  path('', include('Base.urls')),
                  path('Meetme', include('MeetMe.urls')),
                  path('', include('adminpanal.urls')),
                  path('Gallary/', include('Gallary.urls')),
                  path('Blog/', include('admin_blog.urls')),
                  path('LogIn/', include('Registration.urls')),
                  path('Publication',include('UploadFiles.urls')),
                  path('GetInTouch/',include('GetInTouch.urls')),
                  path('Coordinator/',include('Coordinator.urls')),

                  path('', TemplateView.as_view(template_name="socalapp/IndexDemo.html")),
                  path('accounts/', include('allauth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

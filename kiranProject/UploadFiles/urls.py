from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path('',views.viewPublication,name='Publication_page'),
    #url(r'^abs/UploadedFile/P<path>)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
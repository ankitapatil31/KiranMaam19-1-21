from django.urls import path
from . import views


urlpatterns=[
    path('',views.showPhotos,name='Gallary_Photos'),
]
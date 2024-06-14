import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import FileUpload


# Create your views here.


def viewPublication(request):
    obj = FileUpload.objects.all()
    return render(request, 'UploadFiles/ViewPublicationFiles.html', {'ObjFile': obj})


def Download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/FileUpload")
            response['content-dispossition'] = 'inline;filename' + os.path.basename(file_path)
            return response

    raise Http404

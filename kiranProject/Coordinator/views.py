from django.shortcuts import render
from .models import MitraCoordinatePhotos
# Create your views here.


def getCoordinatorInformation(request):
    obj = MitraCoordinatePhotos.objects.all()
    return render(request, 'Coordinator/Mitracoordinator.html', {'obj': obj})

from django.shortcuts import render
from adminpanal.models.Gallary import AddPhotos
from adminpanal.models.Gallary import category
# Create your views here.


def showPhotos(request):
    photos = None
    categorys = category.objects.all()
    categoryID = request.GET.get('category')
    print(categoryID)
    if categoryID:
        photos = AddPhotos.get_all_Photos_by_category(categoryID)
    else:
        photos = AddPhotos.objects.all()
    return render(request,'Gallary/Gallary.html',{'photos':photos,'categorys':categorys})
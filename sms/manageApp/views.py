from django.shortcuts import render, redirect
from . import models


# Create your views here.

def depart_list(request):
    query_set = models.Department.objects.all()

    return render(request, 'depart_list.html', {'query_set': query_set})


def depart_add(request):

    if request.method == 'GET':
        return render(request, 'depart_add.html')

    title = request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/depart/list/")

def depart_del(request):
    
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    
    return redirect('/depart/list/')
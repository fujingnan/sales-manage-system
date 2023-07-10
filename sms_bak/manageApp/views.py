from django.shortcuts import render
from . import models


# Create your views here.

def depart_list(request):
    query_set = models.Department.objects.all()

    return render(request, 'depart_list.html', {'query_set': query_set})


def depart_add(request):

    return render(request, 'depart_add.html')

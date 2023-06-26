from django.shortcuts import render, redirect
from . import models
from .model_card import *
from django import forms
import math
from manageApp.utils.pagination import Pagination


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


def depart_edit(request, id):
    if request.method == 'GET':
        depart_obj = models.Department.objects.filter(id=id).first()
        return render(request, 'depart_edit.html', {'depart_obj': depart_obj})
    title = request.POST.get('title')
    models.Department.objects.filter(id=id).update(title=title)
    return redirect('/depart/list/')


def user_list(request):
    query = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'query': query})


def user_add(request):
    if request.method == 'GET':
        form = UserModel()
        return render(request, 'user_add.html', {'form': form})

    form = UserModel(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')

    return render(request, 'user_add.html', {'form': form})


def user_edit(request, nid):
    raw = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModel(instance=raw)
        return render(request, 'user_edit.html', {'form': form})
    form = UserModel(data=request.POST, instance=raw)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def num_list(request):
    # import random
    # for j in range(300):
    #     models.PrettyNum.objects.create(mobile=str(18812345678+j), price=100, level=random.randint(1, 10), status=random.randint(1, 2))
    q_value = request.GET.get('q', '')
    search_condition = dict()
    if q_value:
        search_condition["mobile__contains"] = q_value

    query = models.PrettyNum.objects.filter(**search_condition).order_by('id')
    pagination_object = Pagination(
        request=request,
        query=query
    )
    finall_query, page_list_show, page, page_total_size = pagination_object.pagination()
    return render(request, 'number_list.html', {'query': finall_query,
                                                'search_data': q_value,
                                                'page_list_show': page_list_show,
                                                'current_page': page,
                                                'page_total_size': page_total_size})


def search_reset(request):
    return redirect('/number/list/')


def num_add(request):
    if request.method == 'GET':
        form = PrettyModel()
        return render(request, 'number_add.html', {'form': form})
    form = PrettyModel(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/number/list/')
    return render(request, 'number_add.html', {'form': form})


def num_edit(request, nid):
    raw = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PrettyEditModel(instance=raw)
        return render(request, 'number_edit.html', {'form': form})
    form = PrettyEditModel(data=request.POST, instance=raw)
    if form.is_valid():
        form.save()
        return redirect('/number/list/')
    return render(request, 'user_edit.html', {'form': form})


def num_delete(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/number/list/')

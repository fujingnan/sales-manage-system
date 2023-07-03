from django.shortcuts import render, redirect
from manageApp.model_card import *


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
from django.shortcuts import render, redirect, HttpResponse
from manageApp.model_card import *
from manageApp.utils.pagination import Pagination
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import random
import json


def order_list(request):
    query = models.Order.objects.all().order_by('-id')
    pagination_object = Pagination(
        request=request,
        query=query
    )
    form = OrderModelForm()
    final_query, page_list_show, page, page_total_size = pagination_object.pagination()
    return render(request, 'order_list.html', {
        'form': form,
        'query': final_query,
        'page_list_show': page_list_show,
        'current_page': page,
        'page_total_size': page_total_size})


@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        admin_id = request.session['info']['id']
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(admin_id) + chr(random.randint(65, 90))
        form.instance.admin_id = admin_id
        form.save()
        return HttpResponse(json.dumps({"status": True}))
    return HttpResponse(json.dumps({"status": False, "error": form.errors}))


def order_delete(request):
    uid = request.GET.get('uid')
    if models.Order.objects.filter(id=uid).exists():
        models.Order.objects.filter(id=uid).delete()
        return HttpResponse(json.dumps({
            'status': True
        }))
    return HttpResponse(json.dumps(
        {
            'status': False,
            'error': '删除失败，数据不存在！'
        }
    ))

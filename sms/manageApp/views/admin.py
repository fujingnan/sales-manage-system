from django.shortcuts import render, redirect
from manageApp.model_card import *
from manageApp.utils.pagination import Pagination
from manageApp.model_card import AdminModel


def admin_list(request):
    q_value = request.GET.get('q', '')
    search_condition = dict()
    if q_value:
        search_condition["username__contains"] = q_value

        query = models.Admin.objects.filter(**search_condition)
    else:
        query = models.Admin.objects.all()
    pagination_object = Pagination(
        request=request,
        query=query
    )
    finall_query, page_list_show, page, page_total_size = pagination_object.pagination()
    return render(request, 'admin_list.html', {'query': finall_query,
                                                'search_data': q_value,
                                                'page_list_show': page_list_show,
                                                'current_page': page,
                                                'page_total_size': page_total_size})

def admin_add(request):
    if request.method == 'GET':
        form = AdminModel()
        return render(request, 'public_add.html', {'form': form, 'entity': '添加管理员'})

    form = AdminModel(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'public_add.html', {'form': form, 'entity': '添加管理员', 'time_type': 'signup_time'})
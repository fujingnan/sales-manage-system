"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manageApp.views import depart, user, pretty, admin, account, order

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_del),
    path('depart/edit/<int:id>/', depart.depart_edit),

    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/edit/<int:nid>/', user.user_edit),
    path('user/delete/<int:nid>', user.user_delete),

    path('number/list/', pretty.num_list),
    path('number/add/', pretty.num_add),
    path('number/edit/<int:nid>', pretty.num_edit),
    path('number/delete/<int:nid>', pretty.num_delete),
    path('search/reset/', pretty.search_reset),

    path('admin/list/', admin.admin_list),
    path('public/add/', admin.admin_add),
    path('admin/edit/<int:nid>/', admin.admin_edit),
    path('admin/delete/<int:nid>', admin.admin_delete),
    path('admin/reset/<int:nid>', admin.admin_reset),
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),

    path('order/list/', order.order_list),
    path('order/add/', order.order_add)

]

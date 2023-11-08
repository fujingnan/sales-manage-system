from django.shortcuts import render, HttpResponse, redirect
from io import BytesIO
from manageApp.model_card import *
from manageApp.utils import generate_code


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        system_code = request.session.get("image_code", "")
        user_code = form.cleaned_data.pop("user_code")
        if system_code.upper() != user_code.upper():
            form.add_error("user_image", '验证码错误')
            return render(request, 'login.html', {'form': form})
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("username", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        return redirect('/admin/list/')
    return render(request, 'login.html', {'form': form})


def logout(request):
    """ 注销 """

    request.session.clear()

    return redirect('/login/')


def image_code(request):
    """ 生成图片验证码 """

    # 调用pillow函数，生成图片
    img, code_string = generate_code.check_code()
    print(code_string)

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给Session设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')

    return HttpResponse(stream.getvalue())

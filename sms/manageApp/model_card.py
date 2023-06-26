from django import forms
from . import models
from django.core.validators import RegexValidator, ValidationError
import re


class UserModel(forms.ModelForm):
    name = forms.CharField(
        label='用户名',
        min_length=1,
        error_messages={
            'required': '名字不能为空！'
        }
    )

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'entry_time', 'depart', 'gender']
        # labels = {
        #     'name': '姓名',
        #     'password': '密码',
        #     'age': '年龄',
        #     'account': '账号',
        #     'entry_time': '账户余额',
        #     'depart': '部门',
        #     'gender': '性别'
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class PrettyModel(forms.ModelForm):
    # mobile = forms.CharField(
    #     label='手机号',
    #     validators=[RegexValidator(r'^1[0-9]\d{9}$', '手机号格式错误')]
    # )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    def clean_mobile(self):
        num = self.cleaned_data['mobile']
        is_exist = models.PrettyNum.objects.filter(mobile=num).exists()
        if is_exist:
            raise ValidationError('手机号已存在！')
        if len(num) < 11:
            raise ValidationError('手机号长度必须是11位！')
        if re.search(r'[a-z|A-Z]', num):
            raise ValidationError('手机号不能包含字母！')
        if not re.search(r'^1[0-9]\d{9}$', num):
            raise ValidationError('手机号必须由11位纯数字组成！')
        return num


class PrettyEditModel(forms.ModelForm):
    # mobile 不可修改
    # mobile = forms.CharField(disabled=True, label='手机号')

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    def clean_mobile(self):
        num = self.cleaned_data['mobile']
        is_exist = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=num).exists()
        if is_exist:
            raise ValidationError('手机号已存在！')
        if len(num) < 11:
            raise ValidationError('手机号长度必须是11位！')
        if re.search(r'[a-z|A-Z]', num):
            raise ValidationError('手机号不能包含字母！')
        if not re.search(r'^1[0-9]\d{9}$', num):
            raise ValidationError('手机号必须由11位纯数字组成！')
        return num
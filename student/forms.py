import json
from django.forms import fields, widgets
from student import models
from django import forms


class SignForm(forms.Form):
    stu_id = forms.CharField(max_length=11, widget=forms.TextInput(attrs={"class": "tpl-form-input","placeholder":"学号"}))
    stu_name = forms.CharField(max_length=3,
                             widget=forms.TextInput(attrs={"class": "tpl-form-input", "placeholder": "姓名"}))
    stu_no = forms.CharField(max_length=18,
                             widget=forms.TextInput(attrs={"class": "tpl-form-input", "placeholder": "身份证"}))

    stu_password = forms.CharField(max_length=11,
                             widget=forms.PasswordInput(attrs={"class": "tpl-form-input", "placeholder": "密码"}))
    stu_password_verify = forms.CharField(max_length=11,
                                   widget=forms.PasswordInput(attrs={"class": "tpl-form-input", "placeholder": "确认密码"}))
    stu_collect = fields.ChoiceField(
        choices=models.CollegeInfo.objects.values_list('college_id','college_name'),
        widget=widgets.Select
    )
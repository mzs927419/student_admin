import datetime

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from student import models
import json
# Create your views here.
from student.forms import SignForm
from student.models import StudentInfo
from student.utils import checkIdcard
from student.PinYin import PinYin

#登陆视图
def login_view(request):
    return render(request, "login.html")

def login(request):
    if request.method == 'POST':
        stu_id = request.POST['stu_id']
        psd = request.POST['stu_password']
        stu = StudentInfo.objects.get(pk=stu_id)
        if stu.stu_password :
            if stu.stu_password == psd:
                return redirect(indexView)
    return render(request, "login.html", {"logerror": "学号或密码错误"})

#注册视图
def sign_view(request):
    return render(request, "sign-up.html", {'obj':SignForm()})

#注册提交
def sign_save(request):
    if request.method == 'POST':
        input_param = SignForm(request.POST)
        if input_param.is_valid():
            data = input_param.clean()
            stu_class =  request.POST['stu_class']
            stutime = request.POST['stu_Time']
            if stutime:
                if stu_class:
                    password_verify = request.POST['stu_password_verify']
                    if password_verify == data['stu_password']:
                        result = checkIdcard(data['stu_no'])
                        if result.get('status'):
                            pyu = PinYin()
                            pyu.load_word()
                            cnname = pyu.hanzi2pinyin_split(string=data['stu_name'], split=" ")
                            classObj = models.ClassInfo.objects.get(pk=stu_class)
                            StudentInfo.objects.create(stu_id=data['stu_id'], stu_name=data['stu_name'],
                                                       stu_no=data['stu_no'],
                                                       stu_password=data['stu_password'],
                                                       stu_class=classObj, stuTime=stutime,stu_sex = result.get('sex'),stu_bir = result.get('birthday'),
                                                       stu_home = result.get('city'),
                                                       createTime=datetime.datetime.now(),
                                                       stu_cnname = cnname)


                            return redirect(login_view)
                        else:
                            return render(request, "sign-up.html", {'obj': input_param, "psdError": result.get('message')})
                    else:
                        return render(request, "sign-up.html", {'obj': input_param, "psdError": "两次密码不一致"})
                else:
                    return render(request, "sign-up.html", {'obj': input_param, "classError": "没有选择班级"})
            else:
                return render(request, "sign-up.html", {'obj': input_param, "timeError": "没有选择入学时间"})
        else:
            error_message = input_param.errors
            return render(request, "sign-up.html", {'obj': input_param, "errors": error_message})
    return redirect(sign_view)#重定向到注册页

#根据学院获取班级 json
def getClass(request):
    collectId = request.POST['collectId']
    data = models.ClassInfo.objects.filter(collect = collectId).values()
    return HttpResponse(json.dumps(list(data)))

def indexView(request):
    return render(request, "index.html")



def stu_list(request):
    stus = models.StudentInfo.objects.all()
    return  render(request,"show.html",{"stus":stus})

def stu_update(request):
    username = request.POST['username']
    id = request.POST['stu_id']
    print("=================")
    print(username)
    print(id)
    print("=================")
    models.StudentInfo.objects.filter(stu_id=id).update(stu_name = username)
    d = {
        "status":200
    }
    return JsonResponse(d)

def jsonn(request):
    jsondata = {
        "a":100,
        "b":200,
        "c":300
    }
    return JsonResponse(jsondata)

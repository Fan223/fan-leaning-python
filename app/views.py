from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    group_id = request.GET.get('group_id')
    return render(request, 'index.html', {'group_id': group_id})

# @csrf_exempt
# def index(request):
#     print(request.GET)
#     print(request.POST)
#
#     # return JsonResponse('返回成功', safe=False)
#     return JsonResponse({'message': '返回成功'})

# from app import models
# def index(request):
#     models.Userinfo.objects.create(name='张三', password='123', age=18)
#
#     models.Userinfo.objects.filter(id=4).delete()
#     models.Userinfo.objects.all().delete()
#
#     data_list = models.Userinfo.objects.all()
#     print(data_list, type(data_list))
#
#     for obj in data_list:
#         print(obj.id, obj.name, obj.password, obj.age)
#
#     filter_list = models.Userinfo.objects.filter(id=1)
#     print(filter_list)
#
#     obj = models.Userinfo.objects.filter(id=1).first()
#     print(obj.id, obj.name, obj.password, obj.age)
#
#     models.Userinfo.objects.filter(id=1).update(age=19)
#     models.Userinfo.objects.all().update(age=15)
#     return HttpResponse('欢迎')

# from django.shortcuts import render, redirect
# def index(request):
#     print(request)
#     name = '张三'
#     roles = ['管理员', '测试']
#     user_info = {'name': '张三', 'age': 28}
#     return render(request, 'index.html', {'n1': name, 'n2': roles, 'n3': user_info})

# def index(request):
#     # 获取请求方式
#     print(request.method)
#     # 获取请求路径
#     print(request.path)
#     # 获取 URL 上传递的值
#     print(request.GET)
#     # 获取请求体中提交的数据
#     print(request.POST)
#     return redirect('https://www.baidu.com')

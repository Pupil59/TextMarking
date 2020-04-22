from register.models import big_user
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import json
from django.contrib.sessions.models import Session
from django.contrib.auth.hashers import check_password


def dispatch(request):
    if request.method in ['POST', 'PUT']:
        request.params = json.load(request.body)
        action = request.params['action']
        if action == 'logout':
            return sign_out(request)
        else:
            return modify_name(request)


def modify_name(request):
    user_id = request.big_user.id
    try:
        user = big_user.objects.get(id=user_id)
        user.name = request.params["user_name"]
        return JsonResponse({
            "ret": 0,
            "msg": "修改成功"
        })
    except big_user.DoesNotExist:
        return JsonResponse({
            "ret": -1,
            "msg": "用户ID不存在"
        })


def sign_out(request):
    logout(request)
    return JsonResponse({
        "ret": 0,
        "msg": "登出成功"
    })


def new_user(request):
    new_id = request.POST.get('user_id')
    count = big_user.objects.filter(id=new_id).count()
    if count > 0:
        return JsonResponse({
            "ret": -1,
            "msg": "用户id已存在"
        })
    else:
        new_password = request.POST.get('password')
        user_name = request.POST.get('user_name')
        user = big_user.objects.create_user(new_id, email=None, password=new_password)
        user.name = user_name
        user.save()
        login(request, user)
        logout(request)
        return JsonResponse({
            "ret": 0,
            "msg": "创建成功"
                             })


def sign_in(request):
    user_id = request.POST.get('user_id')
    user_password = request.POST.get('password')
    user = request.user
    if user is not None:
        if user.is_active is True:
            return JsonResponse({
                "ret": -2,
                "msg": "用户已登录"
            })
    user = authenticate(username=user_id, password=user_password)
    if user is not None:
        login(request, user)
        return JsonResponse({
            "ret": 0,
            "msg": "登陆成功"
        })
    else:
        return JsonResponse({
            "ret": -1,
            "msg": "用户id或密码错误"
        })


def modify_password(request):
    new_password = request.POST.get('new_password')
    cur_password = request.POST.get('cur_password')
    user_id = request.big_user.id
    user = authenticate(id=user_id, password=cur_password)
    if user is not None:
        if cur_password == new_password:
            return JsonResponse({
                "ret": -2,
                "msg": "新密码重复"
            })
        else:
            user.set_password(new_password)
            return JsonResponse({
                "ret": 0,
                "msg": "密码修改成功"
            })
    else:
        return JsonResponse({
            "ret": -1,
            "msg": "当前密码错误"
        })

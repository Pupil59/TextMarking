from register.models import big_user
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import json
from django.contrib.auth.hashers import check_password
from common.models import Project
from project.entity import export_entities
from project.relation import export_relations,export_triads

def dispatch(request):
    if request.method in ['POST', 'PUT']:
        request.params = json.loads(request.body)
        action = request.params['action']
        if action == 'logout':
            return sign_out(request)
        elif action == 'change_name':
            return modify_name(request)
        elif action == 'friend_apply':
            return apply_friends(request)
        elif action == 'friend_apply_accept' or action == 'friend_apply_deny':
            return friend_confirm(request)
        elif action == 'project_invite':
            return invite(request)
        elif action == 'project_invite_accept' or action == 'project_invite_deny':
            return invite_confirm(request)
        elif action == 'remove_fri_project':
            return remove_fri_project(request)
        elif action == 'get_entities_json':
            return export_entities(request)
        elif action == 'get_relations_json':
            return export_relations(request)
        elif action == 'get_triads_json':
            return export_triads(request)
    elif request.method == 'GET':
        request.params = json.loads(request.body)
        action = request.params['action']
        if action == 'get_user_info':
            return get_user_info(request)
        elif action == 'get_friends':
            return get_friends(request)
        elif action == 'get_friends_appli':
            return get_fri_appli(request)


def modify_name(request):
    user = request.user
    if user is not None:
        user.name = request.params["user_name"]
        return JsonResponse({
            "ret": 0,
            "msg": "修改成功"
        })
    else:
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
    count = big_user.objects.filter(username=new_id).count()
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
        # logout(request)
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
            "msg": "登录成功"
        })
    else:
        return JsonResponse({
            "ret": -1,
            "msg": "用户id或密码错误"
        })


def modify_password(request):
    new_password = request.POST.get('new_password')
    cur_password = request.POST.get('cur_password')
    user = request.user
    if check_password(cur_password, user.password):
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


def get_user_info(request):
    user = request.user
    if user is None:
        return JsonResponse({
            "ret": -1,
            "msg": "用户未登录"
        })
    else:
        return JsonResponse({
            "ret": 0,
            "user_name": user.name,
            "user_id": user.username
        })


def get_friends(request):
    user = request.user
    js = {
        'sum': len(user.friends),
        'friend': []
    }
    for friend in user.friends:
        js['friend'].append(friend.username)
        js['friend'].append(friend.name)
    return JsonResponse(json.dumps(js))


def apply_friends(request):
    to_id = request.POST.get('user_id')
    from_user = request.user
    try:
        to_user = big_user.objects.get(username=to_id)
        if from_user in to_user.friends:
            return JsonResponse({
                'ret': -2,
                'msg': "已与该用户成为好友"
            })
        else:
            to_user.friend_apply.append(from_user)
            return JsonResponse({
                "ret": 0,
                "msg": "邀请已发送"
            })
    except big_user.DoesNotExist:
        return JsonResponse({
            "ret": -1,
            "msg": "用户ID不存在"
        })


def friend_confirm(request):
    action = request.POST.get('action')
    if action == 'friend_apply_accept':
        user = request.user
        fri_id = request.POST.get('id')
        fri = big_user.objects.get(username=fri_id)
        user.friends.add(fri)
        user.friend_apply.remove(fri)


def get_fri_appli(request):
    user = request.user
    js = {
        'sum': len(user.friends),
        'friend': []
    }
    for app_user in user.friends:
        js['friend'].append(app_user.username)
        js['friend'].append(app_user.name)
    return JsonResponse(json.dumps(js))


def invite(request):
    user = request.user
    to_id = request.POST.get('friend_id')
    to_user = big_user.objects.get(username=to_id)
    project_id = request.POST.get('friend_id')
    inv_prject = Project.objects.get(id=project_id)
    if to_id not in user.friends:
        return JsonResponse({
            "ret": -1,
            "msg": "未与该用户成为好友"
        })
    to_user.project_invite.add((user, inv_prject))
    return JsonResponse({
        "ret": 0,
        "msg": "邀请已发送"
    })


def invite_confirm(request):
    user = request.user
    action = request.POST.get('action')
    if action == 'project_apply_accept':
        p_id = request.POST.get('project_id')
        proj = Project.objects.get(id=p_id)
        user.fri_project.add(proj)


def get_pro_inv(request):
    user = request.user
    js = {
        'sum': len(user.project_invite),
        'invites': []
            }
    for pro in user.project_invite:
        js['invites'].append({
            'user_id': pro.user.username,
            'user_name': pro.user.name,
            'project_id': pro.id,
            'project_name': pro.name
        })
    return JsonResponse(json.dumps(js))


def get_fri_project(request):
    user = request.user
    js = {
        'sum': len(user.fri_project),
        'invites': []
            }
    for pro in user.fri_project:
        js['invites'].append({
            'user_id': pro.user.username,
            'user_name': pro.user.name,
            'project_id': pro.id,
            'project_name': pro.name
        })
    return JsonResponse(json.dumps(js))


def remove_fri_project(request):
    p_id = request.POST.get('project_id')
    try:
        pro = Project.objects.get(id=p_id)
        user = request.user
        user.fri_project.remove(pro)
        return JsonResponse({
            'ret': 1,
            'msg': "移除成功"
        })
    except Project.DoesNotExist:
        return JsonResponse({
            'ret': -1,
            'msg': "项目id不存在"
        })

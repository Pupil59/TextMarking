from register.models import big_user
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import json
from django.contrib.auth.hashers import check_password
from common.models import Project, Entity, Relation
from django.db.models import F


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
        elif action == 'del_fri':
            return frr_del(request)
    elif request.method == 'GET':
        request.params = request.GET
        action = request.params['action']
        if action == 'get_user_info':
            return get_user_info(request)
        elif action == 'get_friends':
            return get_friends(request)
        elif action == 'get_friends_appli':
            return get_fri_appli(request)
        elif action == 'get_project_invites':
            return get_pro_inv(request)
        elif action == 'get_fri_projects':
            return get_fri_project(request)
        elif action == 'get_triads_json':
            return export_triads(request)
        elif action == 'get_relations_json':
            return export_entities(request)
        elif action == 'get_entities_json':
            return export_relations(request)


def modify_name(request):
    user = request.user
    if user is not None:
        user.name = request.params["user_name"]
        user.save()
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
            user.save()
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
    fri_list = user.friends.all()
    js = {
        'sum': len(fri_list),
        'friends': []
    }
    # print(user.friends)
    for friend in fri_list:
        js['friends'].append(friend.username)
        js['friends'].append(friend.name)
    return JsonResponse(json.dumps(js), safe=False)


def apply_friends(request):
    to_id = request.params['id']
    from_user = request.user
    try:
        to_user = big_user.objects.get(username=to_id)
        fri_list = to_user.friends.all()
        if from_user in fri_list:
            return JsonResponse({
                'ret': -2,
                'msg': "已与该用户成为好友"
            })
        else:
            to_user.friend_apply.add(from_user)
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
    action = request.params['action']
    user = request.user
    fri_id = request.params['id']
    fri = big_user.objects.get(username=fri_id)
    if action == 'friend_apply_accept':
        user.friends.add(fri)
        fri.friends.add(user)
        fri.save()
    user.friend_apply.remove(fri)
    user.save()


def get_fri_appli(request):
    user = request.user
    fri_list = user.friend_apply.all()
    js = {
        'sum': len(fri_list),
        'friends': []
    }
    for app_user in fri_list:
        js['friends'].append({
                'user_id': app_user.username,
                'user_name': app_user.name
             })
    return JsonResponse(json.dumps(js), safe=False)


def invite(request):
    user = request.user
    to_id = request.params['friend_id']
    to_user = big_user.objects.get(username=to_id)
    project_id = request.session.get('project_id')
    inv_prject = Project.objects.get(id=project_id)
    if to_user not in user.friends.all():
        return JsonResponse({
            "ret": -1,
            "msg": "未与该用户成为好友"
        })
    to_user.project_invite.add(inv_prject)
    return JsonResponse({
        "ret": 0,
        "msg": "邀请已发送"
    })


def invite_confirm(request):
    user = request.user
    action = request.params['action']
    p_id = request.params['project_id']
    proj = Project.objects.get(id=p_id)
    if action == 'project_invite_accept':
        user.fri_project.add(proj)
    user.project_invite.remove(proj)
    user.save()


def get_pro_inv(request):
    user = request.user
    pro_list = user.project_invite.all()
    js = {
        'sum': len(pro_list),
        'invites': []
            }
    for pro in pro_list:
        js['invites'].append({
            'user_id': pro.user.username,
            'user_name': pro.user.name,
            'project_id': pro.id,
            'project_name': pro.name
        })
    return JsonResponse(json.dumps(js), safe=False)


def get_fri_project(request):
    user = request.user
    pro_list = user.fri_project.all()
    js = {
        'sum': len(pro_list),
        'invites': []
            }
    for pro in pro_list:
        js['invites'].append({
            'user_id': pro.user.username,
            'user_name': pro.user.name,
            'project_id': pro.id,
            'project_name': pro.name
        })
    return JsonResponse(json.dumps(js), safe=False)


def remove_fri_project(request):
    p_id = request.params['project_id']
    try:
        pro = Project.objects.get(id=p_id)
        user = request.user
        user.fri_project.remove(pro)
        user.save()
        return JsonResponse({
            'ret': 1,
            'msg': "移除成功"
        })
    except Project.DoesNotExist:
        return JsonResponse({
            'ret': -1,
            'msg': "项目id不存在"
        })

#export


def export_triads(request):
    pid = request.session['project_id']

    qs = Relation.objects.filter(project_id=pid) \
        .annotate(
        source_name=F('entity1__name'),
        destination_name=F('entity2__name'),
        source_id=F('entity1__id'),
        target_id=F('entity2__id')
    ) \
        .values(
        'id', 'name', 'source_id', 'source_name', 'target_id', 'destination_name'
    )
    en_list = list(qs)

    js = json.dumps(en_list, sort_keys=False, indent=4, separators=(',', ': '))

    return JsonResponse(js)


def export_relations(request):
    pid = request.session['project_id']
    qs = Relation.objects.filter(project_id=pid).values('id', 'name')

    en_list = list(qs)

    js = json.dumps(en_list, sort_keys=False, indent=4, separators=(',', ': '))
    return JsonResponse(js)


def export_entities(request):
    pid = request.session['project_id']
    qs = Entity.objects.filter(project_id=pid).values('id', 'name')

    en_list = list(qs)

    js = json.dumps(en_list, sort_keys=False, indent=4, separators=(',', ': '))
    return JsonResponse(js)


def frr_del(request):
    user = request.user
    friend_id = request.params['friend_id']
    try:
        fri = big_user.objects.get(username=friend_id)
        if fri not in user.friends.all():
            return JsonResponse({
                "ret": -1,
                "msg": "未与该用户成为好友"
            })
        user.friends.remove(fri)
        fri.friends.remove(user)
        for pro in user.fri_project.all():
            if pro.user == fri:
                user.fri_project.remove(pro)
        for pro in fri.fri_project.all():
            if pro.user == user:
                fri.fri_project.remove(pro)
        user.save()
        fri.save()
        return JsonResponse({
            'ret': 1,
            'msg': '删除成功'
        })
    except big_user.DoesNotExist:
        return JsonResponse({
            "ret": -1,
            "msg": "用户ID不存在"
        })
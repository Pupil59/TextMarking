from django.http import JsonResponse
from django.http import FileResponse
from django.db.models import F
import json

from common.models import Entity, Project
from register.models import big_user


def dispatcher(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/user/index/'},
            status=302)

    if 'project_id' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未进入项目',
            'redirect': '/user/info'},
            status=302)

    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']

    if action == 'list_entity':
        return listentities(request)
    elif action == 'add_entity':
        return addentity(request)
    elif action == 'del_entity':
        return delentity(request)
    elif action == 'modify_entity':
        return modifyentity(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listentities(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录

    # uid = request.user.id
    pid = request.session['project_id']
    qs = Entity.objects.filter(project_id=pid) \
        .annotate(
        user_name=F('user__name')
    ) \
        .values(
        'id', 'name', 'user_name'
    )

    if 'id' in request.params:
        qs = qs.filter(id=request.params['id'])
    if 'name' in request.params:
        qs = qs.filter(name=request.params['name'])

    # 将 QuerySet 对象 转化为 list 类型
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addentity(request):
    info = request.params['data']

    qs = Entity.objects.filter(project_id=request.session['project_id']).values()
    # qs = Entity.objects.filter(user_id=request.user.id).values('id', 'name')
    entities = list(qs)
    for entity in entities:
        if entity['name'] == info['name']:
            username = big_user.objects.get(id=request.user.id)
            return JsonResponse({
                'ret': 1,
                'msg': f'实体名在项目中已经存在，添加者为{username}'
            })

    record = Entity.objects.create(name=info['name'],
                                   project_id=request.session['project_id'],
                                   user_id=request.user.id)

    return JsonResponse({'ret': 0, 'id': record.id})


def modifyentity(request):
    eid = request.params['id']
    newdata = request.params['newdata']

    try:
        entity = Entity.objects.get(id=eid)
    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{eid}`的实体不存在'
        }

    if 'name' in newdata:
        qs = Entity.objects.filter(project_id=request.session['project_id']).values()
        entities = list(qs)
        for entity in entities:
            if entity['name'] == newdata['name']:
                username = big_user.objects.get(id=request.user.id)
                return JsonResponse({
                    'ret': 1,
                    'msg': f'实体名在项目中已经存在，添加者为{username}'
                })
        entity.name = newdata['name']

    # 注意，一定要执行save才能将修改信息保存到数据库
    entity.save()

    return JsonResponse({'ret': 0})


def delentity(request):
    entityid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的实体记录
        entity = Entity.objects.get(id=entityid)
    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{entityid}`的实体不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    entity.delete()

    return JsonResponse({'ret': 0})


def export_entities(request):
    pid = request.session['project_id']
    qs = Entity.objects.filter(project_id=pid).values('id', 'name')

    en_list = list(qs)

    js = json.dumps(en_list, sort_keys=False, indent=4, separators=(',', ': '))

    name = Project.objects.get(id=pid)

    name += '_entities.json'
    file = open(name, 'w')

    file.write(js)

    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + name
    return response

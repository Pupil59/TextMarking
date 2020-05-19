from django.http import JsonResponse
from django.http import FileResponse
from django.db.models import F
import json

from common.models import Relation, Entity, Project, RelType
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
            'redirect': '/user/info/'},
            status=302)

    if request.method == 'GET':
        request.params = request.GET

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']

    if action == 'list_relation':
        return listrelations(request)
    elif action == 'add_relation':
        return addrelation(request)
    elif action == 'del_relation':
        return delrelation(request)
    elif action == 'modify_relation':
        return modifyrelation(request)
    elif action == 'list_type':
        return listtype(request)
    elif action == 'add_type':
        return addtype(request)
    elif action == 'del_type':
        return deltype(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listrelations(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # qs = Relation.objects.values()
    # uid = request.user.id
    pid = request.session['project_id']

    qs = Relation.objects.filter(project_id=pid) \
        .annotate(
        source_name=F('entity1__name'),
        destination_name=F('entity2__name'),
        user_name=F('user__name')
    ) \
        .values(
        'id', 'name', 'source_name', 'destination_name', 'user_name'
    )

    # 将 QuerySet 对象 转化为 list 类型
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addrelation(request):
    info = request.params['data']

    # uid = request.user.id
    pid = request.session['project_id']
    sid = info['source_id']
    tid = info['target_id']

    if sid == tid:
        return JsonResponse({
            'ret': 1,
            'msg': '实体与自身之间不应存在关系'
        })

    try:
        source = Entity.objects.get(id=sid)

    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id为{sid}的关系不存在'
        }

    try:
        Entity.objects.get(id=tid)

    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id为{tid}的关系不存在'
        }

    qs = Relation.objects.filter(project_id=pid).values()
    # qs = Relation.objects.filter(user_id=uid).values()
    relations = list(qs)

    for r in relations:
        if r['entity1_id'] == sid and r['entity2_id'] == tid:
            return JsonResponse({
                'ret': 1,
                'msg': '两者之间已存在其他关系'
            })

    source.symbolSize += 5
    source.save()

    new_relation = Relation.objects.create(name=info['name'],
                                           entity1_id=sid,
                                           entity2_id=tid,
                                           project_id=pid,
                                           user_id=request.user.id)

    return JsonResponse({'ret': 0, 'id': new_relation.id})


def modifyrelation(request):
    rid = request.params['id']
    newdata = request.params['newdata']

    try:
        relation = Relation.objects.get(id=rid)
    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{rid}`的关系不存在'
        }

    if 'name' in newdata:
        relation.name = newdata['name']

    # 注意，一定要执行save才能将修改信息保存到数据库
    relation.save()

    return JsonResponse({'ret': 0})


def delrelation(request):
    relationid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        relation = Relation.objects.get(id=relationid)
    except Relation.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{relationid}`的关系不存在'
        }

    try:
        source = Entity.objects.get(id=relation.entity1_id)

    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{relation.entity1_id}`的关系不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    relation.delete()

    source.symbolSize -= 5
    source.save()

    return JsonResponse({'ret': 0})


def listtype(request):
    pid = request.session['project_id']
    qs = RelType.objects.filter(project_id=pid) \
        .annotate(
        user_name=F('user__name')
    ) \
        .values(
        'id', 'name', 'user_name'
    )

    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addtype(request):
    pid = request.session['project_id']
    uid = request.user.id
    info = request.params['data']

    qs = RelType.objects.filter(project_id=pid).values()
    types = list(qs)

    if info['name'] == '从属' or info['name'] == '并列' or info['name'] == '解释':
        return JsonResponse({
            'ret': 1,
            'msg': '关系名在项目中已经存在'
        })

    for reltype in types:

        if info['name'] == reltype.name:
            username = big_user.objects.get(id=uid)
            return JsonResponse({
                'ret': 1,
                'msg': f'关系名在项目中已经存在，添加者为{username}'
            })

    record = Entity.objects.create(name=info['name'],
                                   project_id=pid,
                                   user_id=uid)

    return JsonResponse({'ret': 0, 'id': record.id})


def deltype(request):
    tid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的实体记录
        reltype = RelType.objects.get(id=tid)
    except RelType.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{tid}`的关系不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    reltype.delete()

    return JsonResponse({'ret': 0})


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

    name = Project.objects.get(id=pid)

    name += '_triads.json'
    file = open(name, 'w')

    file.write(js)

    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + name
    return response


def export_relations(request):
    pid = request.session['project_id']
    qs = Relation.objects.filter(project_id=pid).values('id', 'name')

    en_list = list(qs)

    js = json.dumps(en_list, sort_keys=False, indent=4, separators=(',', ': '))

    name = Project.objects.get(id=pid)

    name += '_relations.json'
    file = open(name, 'w')

    file.write(js)

    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + name
    return response

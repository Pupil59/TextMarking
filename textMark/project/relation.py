from django.http import JsonResponse
from django.db.models import F
import json

from common.models import Relation, Entity


def dispatcher(request):
    if request.user.is_authenticated():
        return JsonResponse({
            'ret': 302,
            'msg': '未登录'},
            status=302)

    if 'project_id' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未进入项目'},
            status=302)
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_relation':
        return listrelations(request)
    elif action == 'add_relation':
        return addrelation(request)
    elif action == 'del_relation':
        return delrelation(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listrelations(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # qs = Relation.objects.values()
    pid = request.session['project_id']

    qs = Relation.objects.filter(project_id=pid) \
        .annotate(
        source_name=F('entity1__name'),
        destination_name=F('entity2__name')
    ) \
        .values(
        'id', 'name', 'source_name', 'destination_name'
    )

    # 将 QuerySet 对象 转化为 list 类型
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addrelation(request):
    info = request.params['data']

    pid = request.session['project_id']
    sname = info['source_name']
    dname = info['destination_name']

    try:
        source = Entity.objects.get(project_id=pid, name=sname)

    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'实体`{sname}`不存在'
        }

    try:
        destination = Entity.objects.get(project_id=pid, name=dname)

    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'实体`{dname}`不存在'
        }

    source.symbolSize += 5
    source.save()

    new_relation = Relation.objects.create(name=info['name'],
                                           entity1_id=source.id,
                                           entity2_id=destination.id,
                                           project_id=pid)

    return JsonResponse({'ret': 0, 'id': new_relation.id})


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
            'msg': f'id 为`{relation.entity1_id}`的实体不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    relation.delete()

    source.symbolSize -= 5
    source.save()

    return JsonResponse({'ret': 0})

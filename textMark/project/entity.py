from django.http import JsonResponse
import json

from common.models import Entity


def dispatcher(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            request.params = request.GET

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
        elif request.method in ['POST', 'DELETE']:
            request.params = json.loads(request.body)

        # 根据不同的action分派给不同的函数进行处理
        action = request.params['action']

        if action == 'list_entity':
            return listentities(request)
        elif action == 'add_entity':
            return addentity(request)
        elif action == 'del_entity':
            return delentity(request)

        else:
            return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
    else:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/user/index/'},
            status=302)


def listentities(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录

    # uid = request.user.id
    pid = request.session['project_id']
    qs = Entity.objects.filter(project_id=pid).values('id', 'name')

    # 将 QuerySet 对象 转化为 list 类型
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addentity(request):
    info = request.params['data']

    qs = Entity.objects.filter(project_id=request.session['project_id']).values()
    entities = list(qs)

    for entity in entities:
        if entity['name'] == info['name']:
            return JsonResponse({
                'ret': 1,
                'msg': '实体名在项目中已经存在'
            })

    record = Entity.objects.create(name=info['name'],
                                   project_id=request.session['project_id'])

    return JsonResponse({'ret': 0, 'id': record.id})


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

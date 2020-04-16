from django.http import JsonResponse
import json

from common.models import Entity


def dispatcher(request):
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
    if action == 'list_entity':
        return listentities(request)
    elif action == 'add_entity':
        return addentity(request)
    elif action == 'del_entity':
        return delentity(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listentities(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Entity.objects.values('id', 'name')

    # 将 QuerySet 对象 转化为 list 类型
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addentity(request):
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Entity.objects.create(name=info['name'])

    return JsonResponse({'ret': 0, 'id': record.id})


def delentity(request):
    entityid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Entity.objects.get(id=entityid)
    except Entity.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{entityid}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    customer.delete()

    return JsonResponse({'ret': 0})

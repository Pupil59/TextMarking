from django.http import JsonResponse
import json

from common.models import Project


def dispatcher(request):
    # 认证
    if request.user.is_authenticated():
        return JsonResponse({
                'ret': 302,
                'msg': '未登录'},
                status=302)

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_project':
        return listprojects(request)
    elif action == 'add_project':
        return addproject(request)
    elif action == 'del_project':
        return delproject(request)
    elif action == 'modify_project':
        return modifyproject(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listprojects(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    uid = request.user.id

    qs = Project.objects.filter(user_id=uid).values('id', 'name')

    # 将 QuerySet 对象 转化为 list 类型
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addproject(request):
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Project.objects.create(name=info['name'],
                                    user_id=info['user_id'])

    return JsonResponse({'ret': 0, 'id': record.id})


def modifyproject(request):
    projectid = request.params['id']
    newdata = request.params['newdata']

    try:
        project = Project.objects.get(id=projectid)
    except Project.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{projectid}`的项目不存在'
        }

    if 'name' in newdata:
        project.name = newdata['name']

    # 注意，一定要执行save才能将修改信息保存到数据库
    project.save()

    return JsonResponse({'ret': 0})


def delproject(request):
    projectid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        project = Project.objects.get(id=projectid)
    except Project.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{projectid}`的项目不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    project.delete()

    return JsonResponse({'ret': 0})


def add_pro_session(request):
    pid = request.params['project_id']

    request.session['project_id'] = pid

    return JsonResponse({'ret': 0})
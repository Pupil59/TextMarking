from django.http import JsonResponse
import json
from django.shortcuts import render

from common.models import Text


def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理
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

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_text':
        return listtexts(request)
    elif action == 'add_text':
        return addtext(request)
    elif action == 'del_text':
        return deltext(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listtexts(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    pid = request.session['project_id']
    qs = Text.objects.filter(project_id=pid).values('id', 'name', 'text')

    # 将 QuerySet 对象 转化为 list 类型
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addtext(request):
    info = request.params['data']

    pid = request.session['project_id']
    record = Text.objects.create(name=info['name'],
                                 text=info['text'],
                                 project_id=pid)

    return JsonResponse({'ret': 0, 'id': record.id})


def deltext(request):
    textid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的文本记录
        text = Text.objects.get(id=textid)
    except Text.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{textid}`的文本不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    text.delete()

    return JsonResponse({'ret': 0})


def import_text(request):
    return render(request, template_name='textMark/import.html')

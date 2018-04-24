#coding=utf-8
from django.contrib import auth as django_auth
import hashlib, base64
from django.http import JsonResponse
from sign.models import Event, Guest
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError, ObjectDoesNotExist


#用户认证
def user_auth(request):
    get_http_auth = request.META.get('HTTP_AUTHORIZATION',b'') #将输入的用户名密码进行加密
    print(get_http_auth)
    auth = get_http_auth.split() #分割成列表，两个元素
    print(auth)
    try:
        auth_parts = base64.b64decode(auth[1]).decode('utf-8').partition(":")
        print(auth_parts)
    except IndexError:
        return "null"
    userid, password = auth_parts[0], auth_parts[2]
    print(userid)
    print(password)
    user = django_auth.authenticate(username=userid, password=password)
    if user is not None and user.is_active:
        django_auth.login(request, user)
        return "success"
    else:
        return "fail"
#发布会查询接口--增加用户认证
def get_event_list(request):
    auth_result = user_auth(request) #调用认证参数
    if auth_result == "null":
        return JsonResponse({'status': 10011, 'message': 'user auth null'})

    if auth_result == "fail":
        return JsonResponse({'status': 10012, 'message': 'user auth fail'})

    eid = request.GET.get("eid", '') #发布会id
    name = request.GET.get("name", '') #发布会名称

    if eid == '' and name == '':
        return JsonResponse({'status':10021,'message':'parameter error'})

    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022,'message':'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status':200,'message':'success','data':event})

    if name != '':
        #可能多条数据
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status':200,'message':'success','data':datas})
        else:
            return JsonResponse({'status':'10022','message':'query result is empty'})
#coding=utf-8
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	#return HttpResponse("<html><h1>hello django!</h1></html>")
	return render(request,"index.html")
	print index.html
def login_action(request):
	print request.method
	if request.method == "POST":
		page_username = request.POST.get("username"," ")
		page_password = request.POST.get("password"," ")
		print page_username
		print page_password
		user = auth.authenticate(username=page_username, password=page_password)
		#if username == 'admin' and password == '123456':
		#response = HttpResponseRedirect('/event_manage/')
		#response.set_cookie('user', username, 3600)
		if user is not None:
			auth.login(request, user) #django自带登录方法

			request.session['user'] = page_username #将session信息记录到浏览器
			response = HttpResponseRedirect('/event_manage/')
			return response
		else:
			return render(request,'index.html',{'error':'username or password error!'})

	else:
		return render(request, 'index.html')

@login_required
def event_manage(request):
	#username = request.COOKIES.get('user', '')
	event_list = Event.objects.all()
	username = request.session.get('user', '') #读取浏览器session
	return render(request,"event_manage.html",{"user":username,
											   "events":event_list})
#发布会名称搜索
@login_required
def search_name(request):
	username = request.session.get('user', '')
	search_name = request.GET.get("name", "") #前端获取到的数据
	if search_name == '':
		event_list = Event.objects.all()
	else:
		event_list = Event.objects.filter(name__contains=search_name) #查询数据库获取到的数据
	return render(request, "event_manage.html",{"user": username,
												 "events": event_list})
#嘉宾管理
@login_required
def guest_manage(request):
	username = request.session.get('user', '')
	guest_list = Guest.objects.all()
	paginator = Paginator(guest_list, 2) #两行分一页
	page = request.GET.get('page') #页面得到的页数 1,2,3
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		#if page is not integer,deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	return render(request,"guest_manage.html",{"user": username,
											   "guests": contacts})

#签到页面
@login_required
def sign_index(request,event_id):
	username = request.session.get('user', '')
	event = get_object_or_404(Event, id=event_id)
	return render(request,"sign_index.html",{'event': event,
						                     "user": username})

#签到动作
@login_required
def sign_index_action(request,event_id):
	event = get_object_or_404(Event, id=event_id)
	phone = request.POST.get('phone','')
	print phone

	if phone is '':
		return render(request, 'sign_index.html', {'hint': '手机号不能为空'})

	result = Guest.objects.filter(phone = phone)
	if not result:
		return render(request, "sign_index.html", {'event':event,
												   'hint': 'phone error.'})
	result = Guest.objects.get(phone=phone,event_id=event_id)
	if not result:
		return render(request, 'sign_index.html', {'event': event,
												   'hint': 'event id or phone error.'})
	result = Guest.objects.get(phone=phone, event_id=event_id)
	print("================" + result.phone)
	if result.sign:
		return render(request, 'sign_index.html', {'event': event,
												   'hint': 'user has sign in.'})
	else:
		Guest.objects.filter(phone=phone, event_id=event_id).update(sign='1')
		return render(request, 'sign_index.html', {'event': event,
												   'hint': 'sign in success!',
												   'guest': result})

@login_required
def logout(request):
	auth.logout(request) #退出登录
	response = HttpResponseRedirect('/index/')
	return response






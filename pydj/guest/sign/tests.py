#coding=utf-8
from django.test import TestCase
from sign.models import Event,Guest
from django.test import Client
from django.contrib.auth.models import User

# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,
                             address='beijing',start_time='2018-03-18 14:00:00')
        Guest.objects.create(id=1,event_id=1,realname='sophy',
                             phone='15810107600',email='sophy@mail.com',sign=False)

    def test_event_models(self):
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address, 'beijing')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone="15810107600")
        self.assertEqual(result.realname, 'sophy')
        self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    '''测试index登录页'''

    def test_index_page_renders_index_template(self):
        '''断言是否用给定的index.html模板响应'''
        response = self.client.get('/index/')
        #print response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class LoginActionTest(TestCase):
    '''测试登录函数'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com','admin123456')
        self.c = Client()

    def test_login_action_username_password_null(self):
        '''用户名密码均为空'''
        test_data = {'username':'','password':''}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''
        test_data = {'username';'abc',}





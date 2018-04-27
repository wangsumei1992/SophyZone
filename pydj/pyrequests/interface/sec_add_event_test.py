#coding=utf-8
import unittest
import requests
import os, sys
import time
import hashlib
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir)
#from db_fixture import test_data

class AddEventTest(unittest.TestCase):
    '''添加发布会'''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_add_event/"
        #app_key
        self.api_key = "&Guest-Bugmaster"
        #当前时间
        now_time = time.time()
        self.client_time = str(now_time).split('.')[0]
        print(self.client_time)
        #sign
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_sign_null(self):
        '''签名参数为空'''
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '', 'time':'', 'sign': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10011)
        self.assertEqual(self.result['message'], 'user sign null')

    def test_add_event_time_out(self):
        '''请求超时'''
        now_time = str(int(self.client_time) - 61)
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '', 'time': now_time, 'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user sign timeout')

    def test_add_event_sign_error(self):
        '''签名错误'''
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '', 'time': self.client_time, 'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10013)
        self.assertEqual(result['message'], 'user sign error')

    def test_add_event_all_null(self):
        '''所有参数为空'''
        payload = {'eid':'','name':'','limit':'','address':'','start_time':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        '''id已经存在'''
        payload= {'eid':1,'name':'railway fabuhui','limit':2000,'address':'shenzhen','start_time':'2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        '''名称已经存在'''
        payload = {'eid':10,'name':'filling','limit':2000,'address':'qinghai','start_time':'2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        '''日期格式错误'''
        payload = {'eid':10,'name':'zizi','limit':2000,'address':'shenzhen','start_time':'2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])

    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid':10,'name':'zizi','limit':2000,'address':'qinghai','start_time':'2017-10-01 12:00:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')

if __name__ == '__main__':
    #test_data.init_data() #初始化接口测试数据
    unittest.main()
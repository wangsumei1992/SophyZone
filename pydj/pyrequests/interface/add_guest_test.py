#coding=utf-8
import os,sys
import unittest, requests
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir)
from db_fixture import test_data

class AddGuestTest(unittest.TestCase):
    '''添加嘉宾测试'''
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_guest/"

    def test_add_guest_all_null(self):
        '''所有参数为空'''
        payload = {'eid':'','realname':'','phone':'','email':''}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')

    def test_add_guest_event_notexist(self):
        '''id不存在'''
        payload = {'eid': '11', 'realname': 'jim', 'phone': '15811507612', 'email': 'jim@mail.com'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'event id null')

    def test_add_guest_event_end(self):
        payload = {'eid': '1', 'realname': 'sgirl', 'phone': '15811507610', 'email': 'silygirl@mail.com'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(result['status'], 10023)
        self.assertEqual(result['message'], 'event status is not available')

    def test_add_guest_event_full(self):
        payload = {'eid': '5', 'realname': 'jim', 'phone': '15811507612', 'email': 'jim@mail.com'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10024)
        self.assertEqual(result['message'], 'event number is full')

    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    test_data.init_data()
    unittest.main()








#coding=utf-8
import requests
import unittest

class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/sec_get_event_list/"
        self.auth_user = ('admin', 'w12345678')

    def test_get_event_auth_null(self):
        '''auth为空'''
        r = requests.get(self.url, params={'eid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10011)
        self.assertEqual(self.result['message'], "user auth null")

    def test_get_event_auth_error(self):
        '''auth错误'''
        r = requests.get(self.url, auth=('abc','111'), params={'eid': ''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10012)
        self.assertEqual(self.result['message'], "user auth fail")

    def test_get_event_eid_null(self):
        '''eid参数为空'''
        r = requests.get(self.url, auth=self.auth_user, params={'eid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], "parameter error")

    def test_get_event_eid_error(self):
        '''eid查询结果为空'''
        r = requests.get(self.url, auth=self.auth_user, params={'eid':'999'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], "parameter error")

    def test_get_event_eid_success(self):
        '''eid查询成功'''
        r = requests.get(self.url, auth=self.auth_user, params={'eid':'3'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], "success")
        self.assertEqual(self.result['data']['name'], "nini")
        self.assertEqual(self.result['data']['address'], "bjstation")

if __name__ == '__main__':
    unittest.main()
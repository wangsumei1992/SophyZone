#coding=utf-8
import requests
import unittest

class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_null(self):
        r = requests.get(self.url, params={'eid':''})
        self.result = r.json()
        print(result)
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], "parameter error")

    def test_get_event_success(self):
        r = requests.get(self.url, params={'eid':'3'})
        self.result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "success")
        self.assertEqual(result['data']['name'], "nini")
        self.assertEqual(result['data']['address'], "bjstation")

if __name__ == '__main__':
    unittest.main()

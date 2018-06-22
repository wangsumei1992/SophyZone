import unittest
import requests

class UserTest(unittest.TestCase):
    """用户查询测试"""

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users'

    def test_user1(self):
        """test user1"""
        r = requests.get(self.base_url+'/1/', auth=('admin', 'w12345678'))
        result = r.json()
        self.assertEqual(result['username'], 'admin')
        #print(result)

    def test_user2(self):
        """test user2"""
        r = requests.get(self.base_url+'/2/', auth=('admin', 'w12345678'))
        result = r.json()
        self.assertEqual(result['username'], 'tom')
        self.assertEqual(result['email'], 'tom@mail.com')
        #print(result)


if __name__ == '__main__':
    unittest.main()
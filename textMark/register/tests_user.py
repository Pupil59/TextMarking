from django.test import TestCase
from rest_framework.test import APIClient
from register.user import new_user
from register.models import big_user
import pprint, json

# Create your tests here.

class registerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_new_user(self):
        self.assertEqual(big_user.objects.count(), 0)
        # 注册
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '13215',
                'password': '123456',
                'user_name': 'crapbag'
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(big_user.objects.count(), 1)

        # 用户id已存在
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '13215',
                'password': '12dda56',
                'user_name': 'peeweeee'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户id已存在')

        # 登录成功
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '13215',
                'password': '123456'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户已登录')

    def test_sign_in_success(self):
        # 注册
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '3146',
                'password': '123456',
                'user_name': 'crapbag'
            }
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(big_user.objects.count(), 1)
        
        # 密码错误--已登录
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '3146',
                'password': '04115456'
            }
        )

        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户已登录')

        # 密码正确--已登录
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '3146',
                'password': '123456'
            }
        )

        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户已登录')

    def test_sign_in_fail(self):
        # 注册
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '3146',
                'password': '123456',
                'user_name': 'crapbag'
            }
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(big_user.objects.count(), 1)
        
        data = {
            'action': 'logout'
        }

        # 登出
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')

        # 密码错误
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '3146',
                'password': '654321'
            }
        )

        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户id或密码错误')

        # id错误
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '2580',
                'password': '123456'
            }
        )

        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户id或密码错误')

    def test_sign_out(self):
        # 注册
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '3146',
                'password': '123456',
                'user_name': 'crapbag'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '创建成功')

        # 已登录
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '3146',
                'password': '123456'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户已登录')

        data= {
            'action': 'logout'
        }

        # 登出
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')

        # 成功登录
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '3146',
                'password': '123456'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登录成功')

    def test_modify_name(self):
        # 注册
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '3146',
                'password': '123456',
                'user_name': 'crapbag'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '创建成功')

        data= {
            'user_id': '3146',
            'action': 'change_name',
            'user_name': 'crapobago'
        }

        # 更改用户名
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '修改成功')

    def test_modify_password(self):
        # 注册
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '3146',
                'password': '123456',
                'user_name': 'crapbag'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '创建成功')

        # 密码错误
        response = self.client.post(
            path= '/user/change_password/',
            data=
            {
                'new_password': 'new_123456',
                'cur_password': 'wrong'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '当前密码错误')

        # 密码重复
        response = self.client.post(
            path= '/user/change_password/',
            data=
            {
                'new_password': '123456',
                'cur_password': '123456'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '新密码重复')

        # 修改成功
        response = self.client.post(
            path= '/user/change_password/',
            data=
            {
                'new_password': 'new_123456',
                'cur_password': '123456'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '密码修改成功')

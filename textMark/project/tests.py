from rest_framework.test import APIClient, APITestCase 
from register.user import *
import requests, pprint, json

class entityTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.assertEqual(big_user.objects.count(), 0)
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
        self.assertEqual(response_content['msg'], '登录成功')

    def test_add_entity(self):

        response = self.client.post(
            path='/api/project/entities',
            data=
            {
                'action':'add_entity',
                'name':'entity1'
            }
        )

        response = self.client.get(
            path='/api/project/entities',
            data=
            {
                'action':'list_entity'
            }
        )

        pprint.pprint(response.content)
        self.assertEqual(response.status_code, 200)

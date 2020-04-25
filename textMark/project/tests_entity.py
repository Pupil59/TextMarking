from rest_framework.test import APIClient, APITestCase 
from common.models import Entity
from register.models import big_user
from django.db.models import Count
import json

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
        
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(big_user.objects.count(), 1)
        self.assertEqual(response_content['msg'], '创建成功')

    def test_add_entity_duplicate(self):
        # 添加实体1
        self.assertEqual(Entity.objects.count(), 0)
        data= {
            'action':'add_entity',
            'name':'entity1'
        }
        response = self.client.post(
            path='/api/project/entities',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Entity.objects.count(), 1)

        # 添加实体2
        data= {
            'action':'add_entity',
            'name':'entity2'
        }
        response = self.client.post(
            path='/api/project/entities',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Entity.objects.count(), 2)

        # 请求实体列表
        response = self.client.get(
            path='/api/project/entities',
            data=
            {
                'action':'list_entity'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(len(response_content['retlist']), 2)        

        # 添加实体--重名
        data= {
            'action':'add_entity',
            'name':'entity2'
        }
        response = self.client.post(
            path='/api/project/entities',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Entity.objects.count(), 2)

    def test_del_entity(self):
        # 添加实体1
        self.assertEqual(Entity.objects.count(), 0)
        data= {
            'action':'add_entity',
            'name':'entity1'
        }
        response = self.client.post(
            path='/api/project/entities',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Entity.objects.count(), 1)
        entity_id_1 = (json.loads(response.content))['id']

        # 添加实体2
        data= {
            'action':'add_entity',
            'name':'entity2'
        }
        response = self.client.post(
            path='/api/project/entities',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Entity.objects.count(), 2)
        entity_id_2 = (json.loads(response.content))['id']

        # 删除实体1
        data= {
            'action': 'del_entity',
            'id': entity_id_1
        }
        self.client.post(
            path='/api/project/entities',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Entity.objects.count(), 1)
        self.assertEqual((json.loads(response.content))['ret'], 0)

        # 删除实体2
        data= {
            'action': 'del_entity',
            'id': entity_id_2
        }
        self.client.post(
            path='/api/project/entities',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Entity.objects.count(), 0)
        self.assertEqual((json.loads(response.content))['ret'], 0)

from rest_framework.test import APIClient, APITestCase
from common.models import Entity, Relation, Project, RelType
from register.models import big_user
from django.db.models import Count
import json


class relationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.assertEqual(big_user.objects.count(), 0)
        # 注册
        response = self.client.post(
            path='/user/register/',
            data=
            {
                'user_id': '3100',
                'password': '123456',
                'user_name': 'dz'
            }
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '创建成功')

        data = {
            'action': 'add_project',
            'data': {
                'name': 'project1'
            }
        }

        response = self.client.post(
            path='/user/projects/',
            data=json.dumps(data),
            content_type='application/json'
        )
        #self.assertEqual(response.status_code, 200)
        self.assertEqual((json.loads(response.content))['ret'], 0)
        self.assertEqual(Project.objects.count(), 1)
        project_id = (json.loads(response.content))['id']

        data = {
            'project_id': project_id
        }
        response = self.client.post(
            path='/api/project/pro_session',
            data=json.dumps(data),
            content_type='application/json'
        )

        # 添加实体1
        self.assertEqual(Entity.objects.count(), 0)
        data = {
            'action': 'add_entity',
            'data': {
                'name': 'entity1'
            }
        }
        response = self.client.post(
            path='/api/project/entities',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Entity.objects.count(), 1)
        self.entity_id_1 = (json.loads(response.content))['id']

        # 添加实体2
        data = {
            'action': 'add_entity',
            'data': {
                'name': 'entity2'
            }
        }
        response = self.client.post(
            path='/api/project/entities',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Entity.objects.count(), 2)
        self.entity_id_2 = (json.loads(response.content))['id']

        # 添加实体3
        data = {
            'action': 'add_entity',
            'data': {
                'name': 'entity3'
            }
        }
        response = self.client.post(
            path='/api/project/entities',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Entity.objects.count(), 3)
        self.entity_id_3 = (json.loads(response.content))['id']

        # 添加实体4
        data = {
            'action': 'add_entity',
            'data': {
                'name': 'entity4'
            }
        }
        response = self.client.post(
            path='/api/project/entities',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Entity.objects.count(), 4)
        self.entity_id_4 = (json.loads(response.content))['id']

    def test_add_relation(self):
        self.assertEqual(Relation.objects.count(), 0)
        # 添加关系1
        data = {
            'action': 'add_relation',
            'data': {
                'source_id': self.entity_id_1,
                'target_id': self.entity_id_2,
                'name': '属于'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 1)

        # 添加关系2
        data = {
            'action': 'add_relation',
            'data': {
                'source_id': self.entity_id_1,
                'target_id': self.entity_id_3,
                'name': '并列'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 2)

        # 请求关系列表
        response = self.client.get(
            path='/api/project/relations',
            data={
                'action': 'list_relation'
            }
        )
        response_content = json.loads(response.content)
        self.assertEqual(len(response_content['retlist']), 2)
        self.assertEqual((json.loads(response.content))['ret'], 0)

    def test_add_relation_duplicate(self):
        self.assertEqual(Relation.objects.count(), 0)
        # 添加关系1
        data = {
            'action': 'add_relation',
            'data': {
                'source_id': self.entity_id_1,
                'target_id': self.entity_id_2,
                'name': '属于'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 1)

        # 添加关系1---两者已存在其他关系
        data = {
            'action': 'add_relation',
            'data': {
                'source_id': self.entity_id_1,
                'target_id': self.entity_id_2,
                'name': '并列'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 1)
        self.assertEqual((json.loads(response.content))['ret'], 1)
        self.assertEqual((json.loads(response.content))['msg'], '两者之间已存在其他关系')
        

        # 添加关系2---实体与自身之间不应存在关系
        data = {
            'action': 'add_relation',
            'data': {
                'source_id': self.entity_id_3,
                'target_id': self.entity_id_3,
                'name': '解释'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 1)

    # 删除实体时实体相关的关系也会被删除
    def test_del_relation(self):
        self.assertEqual(Relation.objects.count(), 0)
        # 添加关系1
        data = {
            'action': 'add_relation',
            'data': {
                'source_id': self.entity_id_1,
                'target_id': self.entity_id_2,
                'name': '属于'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 1)
        response_content = json.loads(response.content)
        relation_id_1 = response_content['id']

        # 添加关系2
        data = {
            'action': 'add_relation',
            'data': {
                'source_id': self.entity_id_1,
                'target_id': self.entity_id_3,
                'name': '并列'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 2)
        response_content = json.loads(response.content)
        relation_id_2 = response_content['id']

        # 添加关系3
        data = {
            'action': 'add_relation',
            'data': {
                'source_id': self.entity_id_3,
                'target_id': self.entity_id_4,
                'name': '递进'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 3)
        response_content = json.loads(response.content)
        relation_id_3 = response_content['id']

        # 删除关系1
        data = {
            'action': 'del_relation',
            'id': relation_id_1
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Relation.objects.count(), 2)

        # 删除实体1---->对应自动删除关系2
        data = {
            'action': 'del_entity',
            'id': self.entity_id_1
        }
        self.client.post(
            path='/api/project/entities',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Entity.objects.count(), 3)
        self.assertEqual(Relation.objects.count(), 1)

        # 删除实体4---->对应自动删除关系3
        data = {
            'action': 'del_entity',
            'id': self.entity_id_4
        }
        self.client.post(
            path='/api/project/entities',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(Entity.objects.count(), 2)
        self.assertEqual(Relation.objects.count(), 0)

    def test_add_del_type(self):
        self.assertEqual(RelType.objects.count(), 0)
        # 添加关系类型1
        data = {
            'action': 'add_type',
            'data': {
                'name': '属于'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(RelType.objects.count(), 1)
        response_content = json.loads(response.content)
        relation_id_1 = response_content['id']
        
        # 删除刚添加的关系类型
        data = {
            'action': 'del_type',
            'id': relation_id_1
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(RelType.objects.count(), 0)
        
        
    def test_list_type(self):
        self.assertEqual(RelType.objects.count(), 0)
        # 添加关系类型1
        data = {
            'action': 'add_type',
            'data': {
                'name': '属于'
            }
        }
        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(RelType.objects.count(), 1)
        response_content = json.loads(response.content)
        relation_id_1 = response_content['id']

        data = {
            'action': 'list_type',
        }

        response = self.client.post(
            path='/api/project/relations',
            data=json.dumps(data),
            content_type='application/json'
        )

        response_content = json.loads(response.content)
        self.assertEqual(response_content['ret'], 0)
        self.assertEqual(len(response_content['retlist']), 4)

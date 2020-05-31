from rest_framework.test import APIClient, APITestCase 
from common.models import Project
from register.models import big_user
from django.db.models import Count
import json

class projectTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.assertEqual(big_user.objects.count(), 0)
        # 注册
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '3100',
                'password': '123456',
                'user_name': 'dz'
            }
        )
        
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(big_user.objects.count(), 1)
        self.assertEqual(response_content['msg'], '创建成功')        
        
        
    def test_add_project_duplicate(self):
        # 添加项目1
        self.assertEqual(Project.objects.count(), 0)
        data= {
            'action':'add_project',
            'data': {
                'name':'project1'
            }
        }
        response = self.client.post(
            path='/user/projects/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual((json.loads(response.content))['ret'], 0)
        self.assertEqual(Project.objects.count(), 1)

        # 添加项目2
        data= {
            'action':'add_project',
            'data': {
                'name':'project2'
            }
        }
        response = self.client.post(
            path='/user/projects/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual((json.loads(response.content))['ret'], 0)
        self.assertEqual(Project.objects.count(), 2)

        # 请求项目列表
        response = self.client.get(
            path='/user/projects/',
            data=
            {
                'action':'list_project'
            }
        )

        response_content = json.loads(response.content)
        self.assertEqual(len(response_content['retlist']), 2)        


    def test_del_project(self):
        # 添加项目1
        self.assertEqual(Project.objects.count(), 0)
        data= {
            'action':'add_project',
            'data': {
                'name':'project1'
            }
        }
        response = self.client.post(
            path='/user/projects/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Project.objects.count(), 1)
        project_id_1 = (json.loads(response.content))['id']

         # 添加项目2
        data= {
            'action':'add_project',
            'data': {
                'name':'project2'
            }
        }
        response = self.client.post(
            path='/user/projects/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Project.objects.count(), 2)
        project_id_2 = (json.loads(response.content))['id']

        # 删除项目1
        data= {
            'action': 'del_project',
            'id': project_id_1
        }
        self.client.post(
            path='/user/projects/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual((json.loads(response.content))['ret'], 0)

        # 删除项目2
        data= {
            'action': 'del_project',
            'id': project_id_2
        }
        self.client.post(
            path='/user/projects/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Project.objects.count(), 0)
        self.assertEqual((json.loads(response.content))['ret'], 0)
    
    def test_modify_project(self):
        self.assertEqual(Project.objects.count(), 0)
        # 添加项目1
        data = {
            'action': 'add_project',
            'data': {
                'name': 'project1'
            }
        }
        response = self.client.post(
            path='/user/projects/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Project.objects.count(), 1)
        project_id_1 = (json.loads(response.content))['id']

        # 修改项目1
        data = {
            'action': 'modify_project',
            'id': project_id_1,
            'newdata': {
                'name': '项目2'
            }
        }
        self.client.post(
            path='/user/projects/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get(id=project_id_1).name, '项目2')
        self.assertEqual((json.loads(response.content))['ret'], 0)

from django.test import TestCase
from rest_framework.test import APIClient
from register.user import new_user
from register.models import big_user
import pprint, json

# Create your tests here.

class registerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        #注册4个新用户为好友和项目邀请做准备
        self.assertEqual(big_user.objects.count(), 0)
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '1',
                'password': '1',
                'user_name': 'user1'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(big_user.objects.count(), 1)
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '2',
                'password': '2',
                'user_name': 'user2'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(big_user.objects.count(), 2)
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '3',
                'password': '3',
                'user_name': 'user3'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(big_user.objects.count(), 3)
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
        response = self.client.post(
            path= '/user/register/',
            data=
            {
                'user_id': '4',
                'password': '4',
                'user_name': 'user4'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(big_user.objects.count(), 4)
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
    def test_friends(self):
        #用户1登录
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '1',
                'password': '1'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登录成功')
        #向其余用户发送好友申请
        data = {
            'action':'friend_apply',
            'id':'2'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        
        data = {
            'action':'friend_apply',
            'id':'3'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        
        data = {
            'action':'friend_apply',
            'id':'4'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        #id不存在的情况
        data = {
            'action':'friend_apply',
            'id':'5'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户ID不存在')
        
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
        #登录其他用户账号同意或拒绝好友申请
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '2',
                'password': '2'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登录成功')
        data = {
            'action':'friend_apply_accept',
            'id':'1'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已接受')
        #此时用户2与用户1成为好友，再次尝试添加用户1为好友
        data = {
            'action':'friend_apply',
            'id':'1'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已与该用户成为好友')
        #再向用户3申请好友
        data = {
            'action':'friend_apply',
            'id':'3'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
        #登录用户3，此时有来自用户1和2的两个申请，测试apply_list
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '3',
                'password': '3'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登录成功')
        data={
                'action':'get_friends_appli'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 2)
        #同意用户1，拒绝用户2
        data = {
            'action':'friend_apply_accept',
            'id':'1'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已接受')
        data = {
            'action':'friend_apply_deny',
            'id':'2'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已拒绝')
        #向用户4申请好友
        data = {
            'action':'friend_apply',
            'id':'4'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        #登录用户4(此时有来自用户1和3的两个申请)
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '4',
                'password': '4'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登录成功')
        #拒绝用户1的申请
        data = {
            'action':'friend_apply_deny',
            'id':'1'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已拒绝')
        #自己再向用户1提出申请
        data = {
            'action':'friend_apply',
            'id':'1'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        #接受用户3的申请
        data = {
            'action':'friend_apply_accept',
            'id':'3'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已接受')
        data = {
            'action':'get_friends'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 1)
        #再删除用户3
        data = {
            'action':'fri_del',
            'id':'3'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已删除')
        #与用户1尚未成为好友
        data = {
            'action':'fri_del',
            'id':'1'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '未该用户成为好友')
        #用户5不存在
        data = {
            'action':'fri_del',
            'id':'5'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户ID不存在')
        #删了3之后无好友
        data = {
            'action':'get_friends'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 0)
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        #回到用户1，此时有用户2和3两个好友以及来自用户4的申请
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '1',
                'password': '1'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '用户已登录')
        #两个好友
        data = {
            'action':'get_friends'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 2)
        #一个申请
        data = {
            'action':'get_friends_appli'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 1)
        #同意用户4的申请
        data = {
            'action':'friend_apply_accept',
            'id':'4'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已接受')
        #好友数量变为3
        data = {
            'action':'get_friends'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 3)
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        #---以上friends相关接口测试完毕---#
        #由于需要保留好友关系，故不再另写测试方法来测试项目邀请部分接口，而是直接沿用上面的好友关系
        
        #登录用户1
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '1',
                'password': '1'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登录成功')
        #添加项目1
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
        project_id_1 = (json.loads(response.content))['id']
        #添加项目2
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
        self.assertEqual(response.status_code, 200)
        self.assertEqual((json.loads(response.content))['ret'], 0)
        self.assertEqual(Project.objects.count(), 2)
        project_id_2 = (json.loads(response.content))['id']
        #向好友用户2发布两个邀请(打开项目后才能邀请，project_id在session中)
        data = {
            'project_id': project_id_1
        }
        response = self.client.post(
            path='/api/project/pro_session',
            data=json.dumps(data),
            content_type='application/json'
        )
        
        data = {
            'action':'project_invite',
            'friend_id': '2',
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        data = {
            'project_id': project_id_2
        }
        response = self.client.post(
            path='/api/project/pro_session',
            data=json.dumps(data),
            content_type='application/json'
        )
        data = {
            'action':'project_invite',
            'friend_id': '2',
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        #向好友用户3发布邀请
        data = {
            'project_id': project_id_1
        }
        response = self.client.post(
            path='/api/project/pro_session',
            data=json.dumps(data),
            content_type='application/json'
        )
        data = {
            'action':'project_invite',
            'friend_id': '3',
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        #向好友用户4发布邀请

        data = {
            'action':'project_invite',
            'friend_id': '4',
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '邀请已发送')
        #向不存在的用户发送邀请

        data = {
            'action':'project_invite',
            'friend_id': '5',
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '未与该用户成为好友')
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
        #登录其他用户账号同意或拒绝项目邀请
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '2',
                'password': '2'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登录成功')
        #有两个邀请，测试invite_list
        data = {
            'action':'get_project_invites'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 2)
        #接受项目1邀请
        data = {
            'action':'project_apply_accept',
            'project_id': project_id_1
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已接受')
        #拒绝项目2邀请
        data = {
            'action':'project_apply_deny',
            'project_id': project_id_2
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已拒绝')
        #可参与编辑好友项目为1个
        data = {
            'action':'get_fri_projects'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 1)
        #登出用户2
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
        #登录用户3，接受来自用户1的邀请
        response = self.client.post(
            path= '/user/sigin/',
            data=
            {
                'user_id': '3',
                'password': '3'
            }
        )
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登录成功')
        #未接受之前可参与好友项目为0
        data = {
            'action':'get_fri_projects'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 0)
        
        data = {
            'action':'project_apply_accept',
            'project_id': project_id_1
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已接受')
        data = {
            'action':'get_fri_projects'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['sum'], 1)
        #登出用户3
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        #登录用户4，测试删除参与的好友项目功能
        data = {
            'action':'project_apply_accept',
            'project_id': project_id_1
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '已接受')
        
        data = {
            'action':'remove_fri_project',
            'project_id': project_id_1
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '移除成功')
        #再一次删除则会id不存在
        data = {
            'action':'remove_fri_project',
            'project_id': project_id_1
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '项目id不存在')
        data = {
            'action': 'logout'
        }
        response = self.client.post(
            path= '/user/other/',
            data= json.dumps(data),
            content_type= 'application/json'
        )
        response_content = json.loads(response.content)
        self.assertEqual(response_content['msg'], '登出成功')
        
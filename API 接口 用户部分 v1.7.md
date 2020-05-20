# API 接口 用户部分及导出 1.7

修改：

​	V1.7 增加拉取好友的项目的API和移除好友项目的API，修改拉取好友邀请的API

​	V1.62 修改拉取好友，拉取好友请求的返回信息的组织方式,修改邀请好友接口，现在前端需要发送被邀请的用户的id。修改拉取项目邀请的返回内容

​	V 1.61 修改了拉取好友和拉取好友的组织方式

​	V 1.6 增加用户好友系统及邀请部分的API，以及导出实体、关系、三元组的api

​	V 1.5

​	增加拉取用户信息的api，暂时拉取用户名和用户id，我到时候跟左正商量下，拉取用户参与的项目。url是user/other/

​	注意一下，登出和修改用户名的url地址是user/other， 之前的user-info里面的地址错了，我给改了。

​	v 1.4

​	修改创建用户的接口

​		现在使用 x-www-form-urlencoded 格式传输数据，提高安全性

​		同时使用新的url进行导航

​		创建用户成功之后会自动登录

​	修改密码部分

​		修改密码时不在需要用户id

​	修改昵称部分：

​		修改昵称的请求不在包含用户id

​	登入部分：

​		新增错误，用户已登入

​	登出部分：

​		登出现在不在需要用户id

​	v1.3

​	修改注册用户、登录和登出部分HTTP请求的请求方法的错误

​	v1.2

​	修改用户系统部分的URL路径

​	v 1.1

​	修改文中错误的文本（三个修改密码）

### 注册

#### 注册新用户

```json
POST /user/register/ HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 中 参数以 格式 x-www-form-urlencoded 存储

需要携带如下参数，

- user_id

  用户名

- user_name

  当前的密码 

- password

  新的密码

其中： userid为用户id，唯一且不可更改

​			user_name为用户昵称可随时更改，

​			password为密码支持数字和大小写

服务端收到之后检查用户id是否已存在，若未存在则创建用户，并登录；否则返回错误信息

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果创建成功，返回如下

```
{
    "ret": 0,
    "msg": "创建成功"
}
```

ret 为0 表示成功

若创建失败则返回如下

```
{
    "ret": -1,
    "msg": "该账号id已使用"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因

### 登录

#### 请求消息

```
POST  /user/signin  HTTP/1.1
Content-Type:   application/x-www-form-urlencoded
```

#### 请求参数

 http 请求消息 body 中 参数以 格式 x-www-form-urlencoded 存储 

需要携带以下参数

`user_id` 字段为用户的id，非用户昵称

`password`字段为用户的密码

服务端接受到该请求后，验证用户id是否存在，进一步验证密码是否正确。



#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果删除成功，返回如下

```
{
    "ret": 0，
    "msg" : "登陆成功"
}
```

ret 为 0 表示成功。

如果登入失败，返回失败的原因，示例如下

```
{
    "ret": -1,    
    "msg": "用户id或密码错误"
}
```

```
{
    "ret": -2,    
    "msg": "用户已登录"
}
```

ret 不为 0 表示失败， msg字段描述失败的原因



### 登出

#### 请求消息

```
PUT  /user/other  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"logout"
}
```

其中

服务端接受到该请求后，验证用户id是否存在，进一步验证用户已登录，若用户已登录则将用户登出。



#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果删除成功，返回如下

```
{
    "ret": 0,
    "msg" : "登出成功"
}
```

ret 为 0 表示成功。

如果登出失败，返回失败的原因，示例如下

```
{
    "ret": -1,    
    "msg": "用户未登录"
}
```

ret 不为 0 表示失败， msg字段描述失败的原因

## 修改密码

### 请求消息

```
POST  /user/change_pasword  HTTP/1.1
Content-Type:   application/x-www-form-urlencoded
```

### 请求参数

http 请求消息 body 中 参数以 格式 x-www-form-urlencoded 存储

需要携带如下参数，

- new_password

  新密码
  
- cur_password

  当前的密码

服务器端得到请求之后先验证当前密码是否正确，若正确则验证新密码是否与当前密码重复，若不重复则替换为新密码

### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
    "ret": 0，
    "msg": "密码修改成功"
}
```

ret 为 0 表示修改成功

如果登录失败，返回失败的原因，示例如下

```
{
    "ret": -1,    
    "msg":  "当前密码错误"
}
```

```
{
    "ret": -2,    
    "msg":  "新密码重复"
}
```



ret 不为 0 表示登录失败， msg字段描述登录失败的原因



## 修改昵称

### 请求消息

```
POST  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

http 响应消息 body 中， 数据以json格式存储，

```
{
	"action":"change_name",
    "user_name" : "穿林北腿蒋中正"
}
```

服务器收到请求后修改用户昵称，要求用户已登录

### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
    "ret": 0,
    "msg": "修改成功"
}
```

ret 为 0 表示修改成功

## 拉取用户信息

### 请求消息

```
GET  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

服务器收到请求后发送用户的昵称和id(好友功能开发中)

```
{
	"action":"get_user_info"
}
```



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
	'ret':0,
    "user_name": "法外狂徒张三",
    "user_id": "zhangsan"
}
```

ret 为 0 表示拉取成功

```
{
	'ret':-1,
	'msg':"用户未登录"
}
```

ret=-1表示拉取失败



## 拉取用户好友信息

### 请求消息

```
GET  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"get_friends"
}
```

服务端接受到该请求后，返回用户的好友列表



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
	'sum':2,
    'friends': [
    	"zhangsan",
    	"法外狂徒张三",
    	"zhaosi",
    	"尼古拉斯赵四"
    ]
}
```

其中sum为好友人数，friends为数组，第一个为好友的id，第二个为好友的昵称，两个一组



## 申请好友

### 请求消息

```
PUT  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"friend_apply",
	"id":"zhangsan"
}
```

其中id为被申请人的id，比如李四向张三申请好友，则id为张三的id

服务端接受到该请求后，查询id是否存在，不存在返回错误，存在则向被申请人发送信息



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
	'ret':0,
    "msg": "邀请已发送"
}
```

若发送的id不存在则返回如下



```
{
	'ret':-1,
    "msg": "id不存在"
}
```

```
{
	'ret':-2,
    "msg": "已与该用户成为好友"
}
```



其中ret=1表示发送的id存在，已向张三发送邀请，ret = -1表示发送的id不存在



## 接受和拒绝好友申请

### 请求消息

```
PUT  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"friend_apply_accept"，
	"id":"zhangsan"
}
```

```
{
	"action":"friend_apply_deny",
	"id":"zhangsan"
}
```

其中action字段为friend_apply_accept为接受邀请，friend_apply_deny为拒绝邀请

id字段为申请人的id

### 响应消息

无

## 拉取好友邀请

### 请求消息

```
GET  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"get_friends_appli"
}
```

服务端接受到该请求后，返回用户的好友申请列表



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
	'sum':2,
    'friends': [
    	{
    	"user_i": "zhangsan",
    	"user_name": "法外狂徒张三",
    	},
    	{
    	"user_i": "zhaosi",
    	"user_name": "尼古拉斯赵四"
		}
    ]
}
```

其中sum为好友人数，friends为数组，第一个为申请者的id，第二个为申请者的昵称，两个一组

## 邀请好友标注项目

### 请求消息

```
PUT  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"project_invite",
	"friend_id": "zhangsan"
}
```

其中project_id为邀请好友参与的项目的id

服务端接受到该请求后，查询id是否存在，不存在返回错误，存在则向被申请人发送信息



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
	'ret':0,
    "msg": "邀请已发送"
}
```

若发送的id不存在则返回如下



```
{
	'ret':-1,
    "msg": "未与该用户成为好友"
}
```





其中ret=1表示发送的id存在，已向张三发送邀请，ret = -1表示发送的id与发送者不是好友，也可能id不存在



## 接受和拒绝项目邀请

### 请求消息

```
PUT  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"project_invite_accept"，
	"project_id":"1234"
}
```

```
{
	"action":"project_invite_deny",
	"project_id":"1234"
}
```

其中action字段为project_invite_accept为接受邀请，project_invite_deny为拒绝邀请

id字段为邀请的项目的id

### 响应消息

无

## 拉取项目邀请

### 请求消息

```
GET  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"get_project_invites"
}
```

服务端接受到该请求后，返回用户的好友申请列表



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
	'sum':1,
    'invites': [
    {
        "user_id": "zhangsan"，
    	"user_name": "法外狂徒张三",
    	"project_id":"1234",
    	"project_name": "project_1"
    	}
    	]
}
```

其中sum为好友人数，user_name为申请者的昵称，user_id为申请者的id

## 拉取用户可参与编辑的好友的项目

### 请求消息

```
GET  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"get_fri_projects"
}
```

服务端接受到该请求后，返回用户的好友申请列表



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
	'sum':1,
    'invites': [
    {
        "user_id": "zhangsan"，
    	"user_name": "法外狂徒张三",
    	"project_id":"1234",
    	"project_name": "project_1"
    	}
    	]
}
```

其中sum为好友人数，user_name为申请者的昵称，user_id为申请者的id,project_id为邀请的项目id，project_name 为邀请的项目的名称

## 移除好友的项目

### 请求消息

```
POST  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"remove_fri_project",
	"project_id": "123"
}
```

服务端接受到该请求后，返回用户的好友申请列表



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
	'ret': 1,
	'msg': "移除成功"
}
```

```
{
	'ret': -1,
	'msg': "项目id不存在"
}
```



## 导出实体文件

### 请求消息

```
GET  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"get_entities_json",
	"id":"1234"
}
```

服务端接受到该请求后，返回导出的实体信息的json文件



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Content-Disposition: attachment;filename= + file_name
```

其中file_name是导出的实体的json文件的名字

### 响应内容

 数据以json文件存储，

## 导出关系文件

### 请求消息

```
GET  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"get_relations_json",
	"id":"1234"
}
```

服务端接受到该请求后，返回导出的关系信息的json文件

其中只含关系的id和name

### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Content-Disposition: attachment;filename= + file_name
```

其中file_name是导出的实体的json文件的名字

### 响应内容

数据以json文件存储，



## 导出实体列表

### 请求消息

```
GET  /user/other  HTTP/1.1
Content-Type: application/json
```

### 请求参数

#### 请求参数

消息体的格式是json，如下示例：

```
{
	"action":"get_triads_json",
	"id":"1234"
}
```

服务端接受到该请求后，返回导出的实体信息的json文件



### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Content-Disposition: attachment;filename= + file_name
```

其中file_name是导出的实体的json文件的名字

### 响应内容

数据以json文件存储，

其中包括关系的id 和name，以及关系所连接的实体的id和name

### 列出所有参与的好友项目

#### 请求消息

```py
GET  /user/other?list_fri_pro  HTTP/1.1
```

#### 请求参数

http 请求消息 url 中 需要携带如下参数，

- action

  填写值为 list_fri_pro

#### 响应消息

```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```json
{
    "sum": 2,
    "retlist": [
        {
            "id": 1,
            "name": "项目1"
        },
        
        {
            "id": 4,
            "name": "project4"
        }
    ]              
}
```

ret 为 0 表示登录成功

retlist 里面包含了所有的项目信息列表。

每个项目信息以如下格式存储

```json
{
   "id": 1,
   "name": "项目1"
}
```


# API接口文档



## 项目部分(textMark/project)

## 项目

### 列出所有项目

#### 请求消息

```py
GET  /user/projects?list_project  HTTP/1.1
```

#### 请求参数

http 请求消息 url 中 需要携带如下参数，

- action

  填写值为 list_project

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
    "ret": 0,
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



### 添加一个项目

#### 请求消息

```py
POST  /user/projects  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加项目的信息

消息体的格式是json，如下示例：

```json
{
    "action":"add_project",
    "data":{
        "name":"项目1"
    }
}
```

其中

`action` 字段固定填写 `add_project` 表示添加一个项目

`data` 字段中存储了要添加的项目的信息

服务端接受到该请求后，应该在系统中增加一个这样的项目。

#### 响应消息

```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```json
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id 为 添加项目的id号。

如果添加失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "项目名已经存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因



### 修改项目信息

#### 请求消息

```py
PUT  /user/projects  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带修改项目的信息

消息体的格式是json，如下示例：

```json
{
    "action":"modify_project",
    "id": 6,
    "newdata":{
        "name":"项目1"
    }
}
```

其中

`action` 字段固定填写 `modify_project` 表示修改一个项目的信息

`id` 字段为要修改的项目的id号

`newdata` 字段中存储了修改后的项目的信息

#### 响应消息

```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果修改失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "项目名已经存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因



### 删除项目信息

#### 请求消息

```py
DELETE  /user/projects  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除项目的id

消息体的格式是json，如下示例：

```json
{
    "action":"del_project",
    "id": 6
}
```

其中

`action` 字段固定填写 `del_project` 表示删除一个项目

`id` 字段为要删除的项目的id号

服务端接受到该请求后，应该在系统中尝试删除该id对应的项目。



#### 响应消息

```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果删除成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果删除失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "id为 566 的项目不存在"
}
```

ret 不为 0 表示失败， msg字段描述删除失败的原因



### 在session中添加项目id

#### 请求消息

```py
POST  /api/project/pro_session  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要添加到session的项目的id

消息体的格式是json，如下示例：

```json
{
    "project_id": 6
}
```

其中

`project_id` 字段为要添加到session的项目的id号

服务端接受到该请求后，应该尝试将该id对应的项目添加到session中。

#### 响应消息

```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果添加失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "id为 566 的项目不存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因





## 文本

### 列出文本

#### 请求消息

```py
GET  /user/texts?list_project  HTTP/1.1
```

#### 请求参数

http 请求消息 url 中 需要携带如下参数，

- action

  填写值为 list_text

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
    "ret": 0,
    "retlist": [
        {
            "id": 1,
            "name": "文本1",
            "text": "blablablablablablablablablablabla"
        }
    ]              
}
```

### 添加文本

#### 请求消息

```py
POST  /user/texts  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加项目的信息

消息体的格式是json，如下示例：

```json
{
    "action":"add_text",
    "data":{
        "name":"文本1",
        "text":"blablablablabla"
    }
}
```

其中

`action` 字段固定填写 `add_text` 表示添加文本

`data` 字段中存储了要添加的文本的信息

服务端接受到该请求后，应该在系统中增加一个这样的文本。

#### 响应消息

```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```json
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id 为 添加文本的id号。

### 删除项目信息

#### 请求消息

```py
DELETE  /user/texts  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除文本的id

消息体的格式是json，如下示例：

```json
{
    "action":"del_texts",
    "id": 6
}
```

其中

`action` 字段固定填写 `del_text` 表示删除一个文本

`id` 字段为要删除的文本的id号

服务端接受到该请求后，应该在系统中尝试删除该id对应的文本。





## 实体

### 列出所有实体

#### 请求消息

```
GET  /api/project/entities  HTTP/1.1
```

#### 请求参数

http 请求消息 url 中 需要携带如下参数，

- action

  必填字段，填写值为 list_entity

- name

  可选字段，填写值为要查找的实体的名称

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```
{
    "ret": 0,
    "retlist": [
        {"id": 1, "name": "实体1", "user_name": "用户1"},
        {"id": 2, "name": "实体2", "user_name": "用户2"}
    ]              
}
```

ret 为 0 表示登录成功

retlist 里面包含了所有的实体信息列表。

每个实体信息以如下格式存储

```
    {"id": 2, "name": "实体2", "user_name": "用户1"}
```



### 添加一个实体

#### 请求消息

```
POST  /api/project/entities  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加实体的信息

消息体的格式是json，如下示例：

```
{
    "action":"add_entity",
    "data":{
        "name": "实体1"
    }
}
```

其中

`action` 字段固定填写 `add_entity` 表示添加一个实体

`data` 字段中存储了要添加的实体的信息

服务端接受到该请求后，应该在系统中增加这样的实体。

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id 为 添加实体的id号。

如果添加失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "实体名在此项目中已经存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因



### 修改实体信息

#### 请求消息

```py
PUT  /api/project/entities  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带修改实体的信息

消息体的格式是json，如下示例：

```json
{
    "action":"modify_entity",
    "id": 6,
    "newdata":{
        "name":"实体1"
    }
}
```

其中

`action` 字段固定填写 `modify_entity` 表示修改一个实体的信息

`id` 字段为要修改的实体的id号

`newdata` 字段中存储了修改后的实体的信息

#### 响应消息

```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果修改失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "实体名已经存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因



### 删除实体信息

#### 请求消息

```
DELETE  /api/project/entities  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除实体的id

消息体的格式是json，如下示例：

```
{
    "action":"del_entity",
    "id": 6
}
```

其中

`action` 字段固定填写 `del_entity` 表示删除一个实体

`id` 字段为要删除的实体的id号

服务端接受到该请求后，应该在系统中尝试删除该id对应的实体。



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
    "ret": 0
}
```

ret 为 0 表示成功。

如果删除失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "id为 566 的实体不存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因





## 关系

### 列出所有关系

#### 请求消息

```
GET  /api/project/relations?action=list_relation  HTTP/1.1
```

#### 请求参数

`action` 字段固定填写 `list_relation` 表示列出关系

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```
{
    "ret": 0,
    "retlist": [
        {id: 1, name: "并列", source_name: "实体1", destination_name: "实体2", user_name: "用户1"},
        {id: 2, name: "从属", source_name: "实体2", destination_name: "实体3", user_name: "用户2"}
    ]              
}
```

ret 为 0 表示登录成功

retlist 里面包含了所有的关系信息列表。

每个关系信息以如下格式存储

```
    {
        id: 2, 
        name: "并列", 
        source_name: "实体1", 
        destination_name: "实体2",
        user_name: "用户2"
    }
```

其中 `source_name` 和 `destination_name` 表示关系的两个实体的名称。



### 添加一个关系

#### 请求消息

```
POST  /api/project/relations HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加关系的信息

消息体的格式是json，如下示例：

```
{
    "action":"add_relation",
    "data":{
        "name":"并列",
        "source_id":"1",
        "target_id":"2"
    }
}
```

其中

`action` 字段固定填写 `add_relation` 表示添加一个关系

`data` 字段中存储了要添加的关系的信息

服务端接受到该请求后，应该在系统中增加这样的关系。

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id 为 添加关系的id号。

如果添加失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "两者之间已经存在其他关系"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因



### 修改关系信息

#### 请求消息

```py
PUT  /api/project/relations  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带修改关系的信息

消息体的格式是json，如下示例：

```json
{
    "action":"modify_relation",
    "id": 6,
    "newdata":{
        "name":"从属"
    }
}
```

其中

`action` 字段固定填写 `modify_relation` 表示修改一个关系的信息

`id` 字段为要修改的关系的id号

`newdata` 字段中存储了修改后的关系的信息

#### 响应消息

```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果修改失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "两者之间已存在此关系"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因



### 删除关系

#### 请求消息

```
DELETE  /api/project/relations  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除关系的id

消息体的格式是json，如下示例：

```
{
    "action":"del_relation",
    "id": 6
}
```

其中

`action` 字段固定填写 `del_relation` 表示删除一个关系

`id` 字段为要删除的关系的id号

服务端接受到该请求后，应该在系统中尝试删除该id对应的关系。



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
    "ret": 0
}
```

ret 为 0 表示成功。

如果删除失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "id为 566 的关系不存在"
}
```

ret 不为 0 表示失败， msg字段描述失败的原因



### 列出关系种类

#### 请求消息

```
GET  /api/project/relations?action=list_type  HTTP/1.1
```

#### 请求参数

http请求消息URL中需要携带如下参数

- action

  固定字段，填写值为list_type

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```
{
    "ret": 0,
    "retlist": [
        {"id": 1, "name": "关系1", "user_name": "用户1"},
        {"id": 2, "name": "关系2", "user_name": "用户2"}
    ]              
}
```

ret 为 0 表示获取成功

retlist 里面包含了所有的关系种类信息列表。

每个关系种类信息以如下格式存储

```
    {"id": 2, "name": "关系2", "user_name": "用户1"}
```



### 添加一个关系种类

#### 请求消息

```
POST  /api/project/relations  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加实体的信息

消息体的格式是json，如下示例：

```
{
    "action":"add_type",
    "data":{
        "name": "关系1"
    }
}
```

其中

`action` 字段固定填写 `add_type` 表示添加一个关系类型

`data` 字段中存储了要添加的关系类型的信息

服务端接受到该请求后，应该在系统中增加这样的关系类型。

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id 为 添加关系类型的id号。

如果添加失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "关系名在此项目中已经存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因



### 删除关系类型信息

#### 请求消息

```
DELETE  /api/project/relations  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除关系类型的id

消息体的格式是json，如下示例：

```
{
    "action":"del_type",
    "id": 6
}
```

其中

`action` 字段固定填写 `del_type` 表示删除一个关系类型

`id` 字段为要删除的关系类型的id号

服务端接受到该请求后，应该在系统中尝试删除该id对应的关系类型。

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
    "ret": 0
}
```

ret 为 0 表示成功。

如果删除失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "id为 566 的关系类型不存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因





## 图谱

### 列出图谱的信息

#### 请求消息

```
GET  /api/project/graph  HTTP/1.1
```

#### 请求参数

http 请求消息**url 中**需要携带如下参数，

- name

  可选字段，表示需要查找的实体的名称

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```
{
	'links': [{'id': 1, 'name': '从属', 'source': 2, 'target': 1, 'user_name':'user_1'}],
 	'nodes': [
 				{'id': 1, 'name': '树', 'symbolSize': 40.0, 'user_name': 'user1', selected': Flase},
 				{'id': 2, 'name': '二叉树', 'symbolSize': 40.0, 'user_name: 'user2',selected': True}
 			],
 	'ret': 0
}
```

ret 为 0 表示登录成功

nodes 里面包含了所有的节点信息列表。

links 里面包含了所有节点间联系的信息列表。

每个节点信息以如下格式存储

```
    {
        id: 2, 
        name: "并列", 
        symbolSize: 40.0,
        selected: False,
        user_name: 用户1
    }
```

每个节点间联系的信息以如下格式存储

```
    {
        id: 2, 
        name: "并列", 
        source: 1,
        target: 2,
        user_name: 用户1
    }
```



## 用户部分(textMark/register)

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
Content-Type:   application/json
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
    	"user_id": "zhangsan",
    	"user_name": "法外狂徒张三",
    	},
    	{
    	"user_id": "zhaosi",
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
	"project_id":"1234"
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
	"action":"get_entities_json"
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
	"action":"get_relations_json"
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
	"action":"get_triads_json"
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

## 删除好友

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
	"action":"fri_del",
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
    "msg": "已删除"
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
    "msg": "未该用户成为好友"
}
```




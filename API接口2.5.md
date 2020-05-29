# api/project接口2.5



## 修改内容

- 增加了实体根据名称查找的功能
- 修改了list_entity的接口
- 增加了在session中添加项目id的接口
- 在实体和用户中添加了添加者的信息，返回信息有变动



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



## 实体

### 列出所有实体

#### 请求消息

```
GET  /api/project/entities  HTTP/1.1
```

#### 请求参数

http 请求消息 body 携带添加实体的信息

消息体的格式是json，如下示例：

```
{
    "action":"list_entity",
    "name":"实体1"
}
```

其中

`action` 字段固定填写 `list_entity` 表示列出实体

`name`字段为要查找的实体的名称 ，为**可选**信息。

服务端接受到该请求后，应该返回实体的信息。

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



## 图谱

### 列出图谱的信息

#### 请求消息

```
GET  /api/project/graph  HTTP/1.1
```

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
	'links': [{'id': 1, 'name': '从属', 'source': 2, 'target': 1}],
 	'nodes': [
 				{'id': 1, 'name': '树', 'symbolSize': 40.0},
 				{'id': 2, 'name': '二叉树', 'symbolSize': 40.0}
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
        symbolSize: 40.0
    }
```

每个节点间联系的信息以如下格式存储

```
    {
        id: 2, 
        name: "并列", 
        source: 1,
        target: 2
    }
```

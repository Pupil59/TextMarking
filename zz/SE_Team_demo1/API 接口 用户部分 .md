# API 接口 用户部分 1.4

修改：

​	v 1.4

​	修改创建用户的接口

​		现在使用 x-www-form-urlencoded 格式传输数据，提高安全性

​		同时使用新的url进行导航

​		创建用户成功之后会自动登录

​	修改密码部分

​		修改密码时不在需要用户id和当前密码

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
PUT  /user/  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带登入id和密码

消息体的格式是json，如下示例：

```
{
	"action":"logout"
}
```

其中

`user_id` 字段为用户的id，非用户昵称

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
    "ret": 0
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

  新的密码

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
    "msg":  "新密码重复"
}
```

ret 不为 0 表示登录失败， msg字段描述登录失败的原因



## 修改昵称

### 请求消息

```
POST  /user/  HTTP/1.1
Content-Type: application/json
```

### 请求参数

http 响应消息 body 中， 数据以json格式存储，

如果修改昵称成功，返回如下

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






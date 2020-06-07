# 在线文本标注系统TextMarking

## 项目地址

- http://114.115.250.237:8000/index/

## 功能描述

- Import:上传本地文本文件或直接粘贴文本内容(一个项目对应一个文本)。
- Text:对于此项目下的文本进行在线标注，支持添加自定义关系类型，鼠标勾选文本内容点击右键进行操作。
- Graph:将添加的实体及相互间的关系使用图形直观显示，鼠标悬停可显示具体信息，点击右键可以进行修改或删除。
- Relation:显示当前所有实体间关系，点击可删除。
- Export:在Text视图下可以将当前的所有实体以及相互关系导出为Json数组并下载至本地，应用于机器学习。
- Invite:添加好友功能和邀请好友协同标注项目(在Graph的具体信息中会注明标注来源)。
- Register/Login:新用户注册账号(使用ID作为唯一标识用于好友的添加与查找)以及老用户登录。
- User_Info:点击头像进入用户信息页面，可以实现登出、修改密码、修改昵称、添加或管理项目以及查看收到的好友申请或项目邀请信息功能。

## 项目结构

#### 服务器部署：

- textMark/SE_Team_demo1:项目的整体settings和urls以及部署至Ubuntu服务器所需的配置文件

- textMark/static_serve:使用collectstatic将所有静态文件收集至一个文件夹，方便使用nginx处理静态请求。

#### 后端API：

- textMark/common:在后端的所有apps中都要用到的通用部分(主要为模型的建立models.py)

- textMark/index:主页部分菜单各项功能(即上面功能描述中的几个按钮)的API。

- textMark/index:项目相关部分的API(包括项目Project、实体Entity、关系Relation、文本Text的增删改查以及关系图Graph的展示)

- textMark/register:用户相关部分的API(用户注册、登录登出、修改信息、好友申请、邀请好友协作项目)

#### 前端页面：

- textMark/templates:利用Django的模板templates实现前端的编写以及通过调用API实现与后端数据库的交互

- textMark/static:模板中html页面所需的静态资源(css、js、images)
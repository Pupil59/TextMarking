from django.urls import path
from register.user import *
from project import project
from index.views import *

urlpatterns = [
    path('index/',showReg),
    path('register/', new_user),
    path('sigin/', sign_in),
    path('change_password/', modify_password),
    path('other/', dispatch),
    path('projects/', project.dispatcher),
    path('info/', showUserInfo),
    path('message/', showMsgList),

    # path('projects', project.dispatcher),
]

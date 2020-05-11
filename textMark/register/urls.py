from django.urls import path
from register.user import *
from project import project
from index.views import showReg,showUserInfo

urlpatterns = [
    path('index/',showReg),
    path('register/', new_user),
    path('sigin/', sign_in),
    path('change_password/', modify_password),
    path('other/', dispatch),
<<<<<<< HEAD
    path('projects', project.dispatcher),
=======
    path('info/', showUserInfo),
    # path('projects', project.dispatcher),
>>>>>>> 65c53cb4f2ae3a8669bb41c8f74e8b671abaeec1
]

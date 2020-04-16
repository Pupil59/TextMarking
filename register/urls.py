from django.urls import path
from register.user import *

urlpatterns = [
    path('register/', new_user),
    path('sigin/', sign_in),
    path('change_password/', modify_name),
    path('other/', dispatch)
]
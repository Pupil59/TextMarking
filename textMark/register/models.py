from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class big_user(AbstractUser):
    name = models.CharField(max_length=40)
    friends = models.ManyToManyField('big_user', related_name='user_friends')
    friend_apply = models.ManyToManyField('big_user', related_name='user_friend_app')
    project_invite = models.ManyToManyField('common.Project', related_name='user_pro_inv')
    fri_project = models.ManyToManyField('common.Project', related_name='user_fri_pro')






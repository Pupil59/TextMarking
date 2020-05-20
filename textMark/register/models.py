from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class big_user(AbstractUser):
    name = models.CharField(max_length=40)
    friends = set()
    friend_apply = set()
    project_invite = set()
    fri_project = set()






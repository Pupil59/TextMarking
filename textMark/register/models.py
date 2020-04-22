from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class big_user(AbstractUser):
    name = models.CharField(max_length=40)






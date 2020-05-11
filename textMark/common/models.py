from django.db import models
from register.models import big_user


class Project(models.Model):
    # 项目名称
    name = models.CharField(max_length=200)

    # 所属用户
    user = models.ForeignKey(big_user, on_delete=models.CASCADE)


class Entity(models.Model):
    # 实体名称
    name = models.CharField(max_length=200)

    # symbolSize
    symbolSize = models.FloatField(default=30)

    # 所属项目
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # 和其他实体的关系，是多对多的关系
    # relations = models.ManyToManyField('self', through='Relation')


class Relation(models.Model):
    # 关系名称
    name = models.CharField(max_length=200)

    # 表示关系是从这个实体发起的，当删除实体时，删除与之对应的所有关系
    entity1 = models.ForeignKey(Entity, related_name='from_entity', on_delete=models.CASCADE)

    # 表示关系的目标实体，当删除实体时，删除与之对应的所有关系
    entity2 = models.ForeignKey(Entity, related_name='to_entity', on_delete=models.CASCADE)

    # 所属项目
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

# class Text(models.Model):
#     # 文档名称
#     name = models.CharField(max_length=200)
#
#     # 所属项目
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#
#     # 文档路径
#     text = models.FileField(upload_to='/%Y/%m/%d')

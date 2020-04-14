from django.db import models


class Entity(models.Model):
    # 实体名称
    name = models.CharField(max_length=200)

    # 和其他实体的关系，是多对多的关系
    # relations = models.ManyToManyField('self', through='Relation')


class Relation(models.Model):
    # 关系名称
    name = models.CharField(max_length=200)

    # 表示关系是从这个实体发起的，当删除实体时，删除与之对应的所有关系
    source = models.ForeignKey(Entity, related_name='source', on_delete=models.CASCADE)

    # 表示关系的目标实体，当删除实体时，删除与之对应的所有关系
    destination = models.ForeignKey(Entity, related_name='destination', on_delete=models.CASCADE)

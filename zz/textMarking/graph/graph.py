from django.http import JsonResponse
from django.db.models import F

from common.models import Entity, Relation


def listgraph(request):
    qs_entity = Entity.objects.values()
    qs_relation = Relation.objects \
        .annotate(
            source=F('entity1__id'),
            target=F('entity2__id')
        ) \
        .values(
            'id', 'name', 'source', 'target'
        )

    nodes = list(qs_entity)
    links = list(qs_relation)

    return JsonResponse({'ret': 0, 'nodes': nodes, 'links': links})

from django.urls import path
from project import graph, entity, relation, project

urlpatterns = [
    path('entities', entity.dispatcher),
    path('relations', relation.dispatcher),
    path('graph', graph.listgraph),
    # path('texts', text.dispatcher),
    path('pro_session', project.add_pro_session),
]

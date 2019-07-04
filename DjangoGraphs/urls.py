from django.urls import path

from .views import *

urlpatterns = [

    path('', views.index, name='index'),

    path('view/graph/<int:pk>/', views.view_graph, name='view_graph'),

    path('new/graph/', new.GraphCreate.as_view(), name='new_graph'),
    path('new/graph_selector/', new.GraphSelectorCreate.as_view(), name='new_graph_selector'),
    path('new/type/', new.TypeCreate.as_view(), name='new_type'),
    path('new/instance/', new.InstanceCreate.as_view(), name='new_instance'),

    path('list/graph/', lists.graph, name='list_graph'),
    path('list/graph_selector/', lists.graph_selector, name='list_graph_selector'),
    path('list/type/', lists.type, name='list_type'),
    path('list/instance/', lists.instance, name='list_instance'),

    path('edit/graph/<int:pk>/', edit.GraphUpdate.as_view(), name='edit_graph'),
    path('edit/graph_selector/<int:pk>/', edit.GraphSelectorUpdate.as_view(), name='edit_graph_selector'),
    path('edit/type/<int:pk>/', edit.TypeUpdate.as_view(), name='edit_type'),
    path('edit/instance/<int:pk>/', edit.InstanceUpdate.as_view(), name='edit_instance'),

    path('delete/graph/<int:pk>/', edit.GraphDelete.as_view(), name='delete_graph'),
    path('delete/graph_selector/<int:pk>/', edit.GraphSelectorDelete.as_view(), name='delete_graph_selector'),
    path('delete/type/<int:pk>/', edit.TypeDelete.as_view(), name='delete_type'),
    path('delete/instance/<int:pk>/', edit.InstanceDelete.as_view(), name='delete_instance'),

    path('redirect/delete/<slug:name>/<int:pk>/', edit.delete_redirect, name='redirect_delete'),
]

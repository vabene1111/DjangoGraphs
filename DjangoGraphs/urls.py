from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from .views import *

router = routers.DefaultRouter()
router.register(r'entry', api.DataEntrySet)

urlpatterns = [

    path('', views.index, name='index'),

    path('account', views.account, name='account'),
    path('i18n/', include('django.conf.urls.i18n')),

    path('system', views.system, name='system'),
    path('system/type', views.system_change_type, name='system_type'),
    path('system/instance', views.system_change_instance, name='system_instance'),

    path('view/graph/<int:pk>/', views.view_graph, name='view_graph'),
    path('view/graph_advanced/<int:pk>/', views.view_graph_advanced, name='view_graph_advanced'),

    path('new/graph/', new.GraphCreate.as_view(), name='new_graph'),
    path('new/display/', new.DisplayCreate.as_view(), name='new_display'),
    path('new/graph_selector/', new.GraphSelectorCreate.as_view(), name='new_graph_selector'),
    path('new/type/', new.TypeCreate.as_view(), name='new_type'),
    path('new/instance/', new.InstanceCreate.as_view(), name='new_instance'),

    path('list/graph/', lists.graph, name='list_graph'),
    path('list/display/', lists.display, name='list_display'),
    path('list/graph_selector/', lists.graph_selector, name='list_graph_selector'),
    path('list/type/', lists.type, name='list_type'),
    path('list/instance/', lists.instance, name='list_instance'),

    path('edit/graph/<int:pk>/', edit.GraphUpdate.as_view(), name='edit_graph'),
    path('edit/display/<int:pk>/', edit.DisplayUpdate.as_view(), name='edit_display'),
    path('edit/graph_selector/<int:pk>/', edit.GraphSelectorUpdate.as_view(), name='edit_graph_selector'),
    path('edit/type/<int:pk>/', edit.TypeUpdate.as_view(), name='edit_type'),
    path('edit/instance/<int:pk>/', edit.InstanceUpdate.as_view(), name='edit_instance'),

    path('delete/graph/<int:pk>/', edit.GraphDelete.as_view(), name='delete_graph'),
    path('delete/display/<int:pk>/', edit.DisplayDelete.as_view(), name='delete_display'),
    path('delete/graph_selector/<int:pk>/', edit.GraphSelectorDelete.as_view(), name='delete_graph_selector'),
    path('delete/type/<int:pk>/', edit.TypeDelete.as_view(), name='delete_type'),
    path('delete/instance/<int:pk>/', edit.InstanceDelete.as_view(), name='delete_instance'),

    path('redirect/delete/<slug:name>/<int:pk>/', edit.delete_redirect, name='redirect_delete'),

    # API
    path('api/docs', include_docs_urls(title='DjangoGraphs API', public=False), name='api_docs'),
    path('api/auth/', include('rest_framework.urls')),

    path('api/graph_data/', GraphDataView.as_view(), name='api_graph_data'),

    path('api/', include(router.urls)),
]

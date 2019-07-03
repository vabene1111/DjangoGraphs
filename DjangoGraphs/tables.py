import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from django.utils.translation import gettext as _

from .models import *


class GraphTable(tables.Table):
    id = tables.LinkColumn('edit_graph', args=[A('id')])

    class Meta:
        model = Graph
        fields = ('id', 'name')


class GraphSelectorTable(tables.Table):
    id = tables.LinkColumn('edit_graph_selector', args=[A('id')])

    class Meta:
        model = GraphSelector
        fields = ('id', 'type', 'instance')


class TypeTable(tables.Table):
    id = tables.LinkColumn('edit_type', args=[A('id')])

    class Meta:
        model = Type
        fields = ('id', 'name')


class InstanceTable(tables.Table):
    id = tables.LinkColumn('edit_instance', args=[A('id')])

    class Meta:
        model = Instance
        fields = ('id', 'name')

import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from django.utils.translation import gettext as _

from .models import *


class GraphTable(tables.Table):
    id = tables.LinkColumn('edit_graph', args=[A('id')])

    options = tables.TemplateColumn(
        "<a href='{% url 'delete_graph' record.id %}' class='btn btn-danger'><i class='fas fa-trash'></i></a> " +
        "<a href='{% url 'view_graph' record.id %}' class='btn btn-success'><i class='fas fa-eye'></i></a> " +
        "<a href='{% url 'view_graph_advanced' record.id %}' class='btn btn-info'><i class='fas fa-binoculars'></i></a>",
        verbose_name=_('Options'))

    class Meta:
        model = Graph
        fields = ('id', 'name', 'public', 'dashboard')


class GraphSelectorTable(tables.Table):
    id = tables.LinkColumn('edit_graph_selector', args=[A('id')])

    options = tables.TemplateColumn(
        "<a href='{% url 'delete_graph_selector' record.id %}' class='btn btn-danger'><i class='fas fa-trash'></i></a>",
        verbose_name=_('Options'))

    class Meta:
        model = GraphSelector
        fields = ('id', 'name', 'type', 'instance')


class TypeTable(tables.Table):
    id = tables.LinkColumn('edit_type', args=[A('id')])

    options = tables.TemplateColumn(
        "<a href='{% url 'delete_type' record.id %}' class='btn btn-danger'><i class='fas fa-trash'></i></a>",
        verbose_name=_('Options'))

    class Meta:
        model = Type
        fields = ('id', 'name')


class InstanceTable(tables.Table):
    id = tables.LinkColumn('edit_instance', args=[A('id')])

    options = tables.TemplateColumn(
        "<a href='{% url 'delete_instance' record.id %}' class='btn btn-danger'><i class='fas fa-trash'></i></a>",
        verbose_name=_('Options'))

    class Meta:
        model = Instance
        fields = ('id', 'name')


class DisplayTable(tables.Table):
    id = tables.LinkColumn('edit_display', args=[A('id')])

    options = tables.TemplateColumn(
        "<a href='{% url 'delete_display' record.id %}' class='btn btn-danger'><i class='fas fa-trash'></i></a>",
        verbose_name=_('Options'))

    class Meta:
        model = Display
        fields = ('id', 'name')

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.translation import gettext as _

from ..forms import *
from ..models import *
from ..tables import *


def graph(request):
    table = GraphTable(Graph.objects.all())
    if not request.user.is_authenticated:
        table = GraphTable(Graph.objects.filter(public=True).all())

    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'generic/list_template.html', {'title': _("Graphs"), 'table': table})


@login_required
def graph_selector(request):
    table = GraphSelectorTable(GraphSelector.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'generic/list_template.html', {'title': _("Graph Selectors"), 'table': table})


@login_required
def type(request):
    table = TypeTable(Type.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'generic/list_template.html', {'title': _("Types"), 'table': table})


@login_required
def instance(request):
    table = InstanceTable(Instance.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'generic/list_template.html', {'title': _("Instances"), 'table': table})

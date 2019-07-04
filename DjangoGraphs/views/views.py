from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from DjangoGraphs.models import Graph, DataEntry


def index(request):
    graphs = Graph.objects.filter(dashboard=True).all()

    if not request.user.is_authenticated:
        graphs = Graph.objects.filter(dashboard=True, public=True).all()

    graph_data = {}
    for g in graphs:
        graph_data[g.pk] = []
        for s in g.selector.all():
            graph_data[g.pk].append({'id': s.pk,
                                     'label': s.name,
                                     'color': s.color,
                                     'unit': s.type.unit,
                                     'data': DataEntry.objects.filter(type=s.type, instance=s.instance).all()})

    return render(request, 'index.html', {'graphs': graphs, 'graph_data': graph_data})


def view_graph(request, pk):
    graph = Graph.objects.get(pk=pk)

    if not request.user.is_authenticated:
        if not graph.public:
            return HttpResponseRedirect(reverse('login'))

    graph_data = []
    for s in graph.selector.all():
        graph_data.append({'id': s.pk,
                           'label': s.name,
                           'color': s.color,
                           'unit': s.type.unit,
                           'data': DataEntry.objects.filter(type=s.type, instance=s.instance).all()})

    return render(request, 'graph_view.html', {'graph': graph, 'graph_data': graph_data})


def view_graph_advanced(request, pk):
    graph = Graph.objects.get(pk=pk)

    if not request.user.is_authenticated:
        if not graph.public:
            return HttpResponseRedirect(reverse('login'))

    graph_data = []
    for s in graph.selector.all():
        graph_data.append({'id': s.pk,
                           'label': s.name,
                           'color': s.color,
                           'unit': s.type.unit,
                           'data': DataEntry.objects.filter(type=s.type, instance=s.instance).all()})

    return render(request, 'advanced_graph_view.html', {'graph': graph, 'graph_data': graph_data})

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
from django.urls import reverse, reverse_lazy

from DjangoGraphs.forms import SettingsForm
from DjangoGraphs.models import Graph, DataEntry, Display, Settings


def index(request):
    graphs = Graph.objects.filter(dashboard=True).all()
    displays = Display.objects.filter(dashboard=True).all()

    if not request.user.is_authenticated:
        graphs = Graph.objects.filter(dashboard=True, public=True).all()
        displays = Display.objects.filter(dashboard=True, public=True).all()

    time_threshold = datetime.now() - timedelta(hours=24)

    graph_data = {}
    for g in graphs:
        graph_data[g.pk] = []
        for s in g.selector.all():
            label = s.name
            if s.title:
                label = s.title

            graph_data[g.pk].append({'id': s.pk,
                                     'label': label,
                                     'color': s.color,
                                     'unit': s.type.unit,
                                     'data': DataEntry.objects.filter(type=s.type, instance=s.instance, timestamp__gt=time_threshold).all()})

    display_data = []
    for d in displays:
        entry = DataEntry.objects.filter(type=d.selector.type, instance=d.selector.instance).latest('timestamp')

        label = d.name
        if d.title:
            label = d.title

        display_data.append({
            'id': d.pk,
            'label': label,
            'value': entry.value,
            'unit': d.selector.type.unit,
        })

    return render(request, 'index.html', {'graphs': graphs, 'graph_data': graph_data, 'display_data': display_data})


def view_graph(request, pk):
    graph = Graph.objects.get(pk=pk)

    time_threshold = datetime.now() - timedelta(hours=24)

    if not request.user.is_authenticated:
        if not graph.public:
            return HttpResponseRedirect(reverse('login'))

    graph_data = []
    for s in graph.selector.all():
        label = s.name
        if s.title:
            label = s.title

        graph_data.append({'id': s.pk,
                           'label': label,
                           'color': s.color,
                           'unit': s.type.unit,
                           'data': DataEntry.objects.filter(type=s.type, instance=s.instance, timestamp__gt=time_threshold).all()})

    return render(request, 'graph_view.html', {'graph': graph, 'graph_data': graph_data})


def view_graph_advanced(request, pk):
    graph = Graph.objects.get(pk=pk)

    if not request.user.is_authenticated:
        if not graph.public:
            return HttpResponseRedirect(reverse('login'))

    graph_data = []
    for s in graph.selector.all():
        label = s.name
        if s.title:
            label = s.title

        graph_data.append({'id': s.pk,
                           'label': label,
                           'color': s.color,
                           'unit': s.type.unit,
                           'data': DataEntry.objects.filter(type=s.type, instance=s.instance).all()})

    return render(request, 'advanced_graph_view.html', {'graph': graph, 'graph_data': graph_data})


@login_required
def system(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse_lazy('list_graph'))

    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            settings = Settings.objects.get(pk=1)
            settings.title = form.cleaned_data['title']
            settings.save()

            return HttpResponseRedirect(reverse_lazy('system'))

    else:
        settings = Settings.objects.get(pk=1)
        form = SettingsForm(instance=settings)

    return render(request, 'system.html', {'form': form})

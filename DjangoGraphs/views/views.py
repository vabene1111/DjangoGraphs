from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime, timedelta

from django.utils.translation import gettext as _

from django.urls import reverse, reverse_lazy

from DjangoGraphs.forms import SettingsForm, InstanceChangeForm, TypeChangeForm
from DjangoGraphs.models import Graph, DataEntry, Display, Settings


def index(request):
    graphs = Graph.objects.filter(dashboard=True).order_by('-order', 'pk').all()
    displays = Display.objects.filter(dashboard=True).order_by('-order', 'pk').all()

    if not request.user.is_authenticated:
        graphs = Graph.objects.filter(dashboard=True, public=True).order_by('-order', 'pk').all()
        displays = Display.objects.filter(dashboard=True, public=True).order_by('-order', 'pk').all()

    time_threshold = datetime.now() - timedelta(hours=24)

    graph_data = {}
    for g in graphs:
        graph_data[g.pk] = []
        for s in g.selector.order_by('-order', 'pk').all():
            label = s.name
            if s.title:
                label = s.title

            graph_data[g.pk].append({'id': s.pk,
                                     'label': label,
                                     'color': s.color,
                                     'unit': s.type.unit,
                                     'data': DataEntry.objects.filter(type=s.type, instance=s.instance, timestamp__gt=time_threshold).order_by('timestamp').all()})

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
    for s in graph.selector.order_by('-order', 'pk').all():
        label = s.name
        if s.title:
            label = s.title

        graph_data.append({'id': s.pk,
                           'label': label,
                           'color': s.color,
                           'unit': s.type.unit,
                           'data': DataEntry.objects.filter(type=s.type, instance=s.instance, timestamp__gt=time_threshold).order_by('timestamp').all()})

    return render(request, 'graph_view.html', {'graph': graph, 'graph_data': graph_data})


def view_graph_advanced(request, pk):
    graph = Graph.objects.get(pk=pk)

    if not request.user.is_authenticated:
        if not graph.public:
            return HttpResponseRedirect(reverse('login'))

    graph_data = []
    for s in graph.selector.order_by('-order', 'pk').all():
        label = s.name
        if s.title:
            label = s.title

        graph_data.append({'id': s.pk,
                           'label': label,
                           'color': s.color,
                           'unit': s.type.unit,
                           'data': DataEntry.objects.filter(type=s.type, instance=s.instance).order_by('timestamp').all()})

    return render(request, 'advanced_graph_view.html', {'graph': graph, 'graph_data': graph_data})


@login_required
def system(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse_lazy('index'))

    type_form = TypeChangeForm()
    instance_form = InstanceChangeForm()

    if request.method == 'POST':
        settings_form = SettingsForm(request.POST)
        if settings_form.is_valid():
            settings = Settings.objects.get(pk=1)
            settings.title = settings_form.cleaned_data['title']
            settings.save()
            # TODO alerts
            return HttpResponseRedirect(reverse_lazy('system'))
        # TODO alerts
    else:
        settings = Settings.objects.get(pk=1)
        settings_form = SettingsForm(instance=settings)

    return render(request, 'system.html', {'settings_form': settings_form, 'type_form': type_form, 'instance_form': instance_form})


@login_required
def system_change_type(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse_lazy('index'))

    if request.method == 'POST':
        type_form = TypeChangeForm(request.POST)
        if type_form.is_valid():
            DataEntry.objects.filter(type=type_form.cleaned_data['old_type']).update(type=type_form.cleaned_data['new_type'])
            messages.add_message(request, messages.SUCCESS, _('Types updated!'))

            return HttpResponseRedirect(reverse_lazy('system'))

    return HttpResponseRedirect(reverse_lazy('system'))


@login_required
def system_change_instance(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse_lazy('index'))

    if request.method == 'POST':
        instance_form = InstanceChangeForm(request.POST)
        if instance_form.is_valid():
            DataEntry.objects.filter(instance=instance_form.cleaned_data['old_instance']).update(instance=instance_form.cleaned_data['new_instance'])
            messages.add_message(request, messages.SUCCESS, _('Instances updated!'))

            return HttpResponseRedirect(reverse_lazy('system'))

    return HttpResponseRedirect(reverse_lazy('system'))

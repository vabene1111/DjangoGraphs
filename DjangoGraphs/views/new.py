from braces.views import GroupRequiredMixin, LoginRequiredMixin

from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView

from ..forms import *
from ..models import *


class GraphUserGroupRequiredMixin(GroupRequiredMixin):
    group_required = [u"User", ]


class GraphCreate(LoginRequiredMixin, GraphUserGroupRequiredMixin, CreateView):
    template_name = "generic/new_template.html"
    model = Graph
    form_class = GraphForm

    success_url = reverse_lazy('list_graph')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(GraphCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(GraphCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(GraphCreate, self).get_context_data(**kwargs)
        context['title'] = _("Graph")
        return context


class GraphSelectorCreate(LoginRequiredMixin, GraphUserGroupRequiredMixin, CreateView):
    template_name = "generic/new_template.html"
    model = GraphSelector
    form_class = GraphSelectorForm

    success_url = reverse_lazy('list_graph_selector')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(GraphSelectorCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(GraphSelectorCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(GraphSelectorCreate, self).get_context_data(**kwargs)
        context['title'] = _("Graph Selector")
        return context


class TypeCreate(LoginRequiredMixin, GraphUserGroupRequiredMixin, CreateView):
    template_name = "generic/new_template.html"
    model = Type
    form_class = TypeForm

    success_url = reverse_lazy('list_type')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(TypeCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(TypeCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(TypeCreate, self).get_context_data(**kwargs)
        context['title'] = _("Type")
        return context


class InstanceCreate(LoginRequiredMixin, GraphUserGroupRequiredMixin, CreateView):
    template_name = "generic/new_template.html"
    model = Instance
    form_class = InstanceForm

    success_url = reverse_lazy('list_instance')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(InstanceCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(InstanceCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(InstanceCreate, self).get_context_data(**kwargs)
        context['title'] = _("Display")
        return context


class DisplayCreate(LoginRequiredMixin, GraphUserGroupRequiredMixin, CreateView):
    template_name = "generic/new_template.html"
    model = Display
    form_class = DisplayForm

    success_url = reverse_lazy('list_display')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(DisplayCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(DisplayCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(DisplayCreate, self).get_context_data(**kwargs)
        context['title'] = _("Display")
        return context

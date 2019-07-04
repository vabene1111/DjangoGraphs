from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.contrib import messages

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _
from django.views.generic import UpdateView, DeleteView

from ..forms import *
from ..models import *


class GraphUserGroupRequiredMixin(GroupRequiredMixin):
    group_required = [u"User", ]


class GraphUpdate(LoginRequiredMixin, GraphUserGroupRequiredMixin, UpdateView):
    model = Graph
    form_class = GraphForm
    template_name = "generic/edit_template.html"

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(GraphUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(GraphUpdate, self).form_invalid(form)

    def get_success_url(self):
        return reverse('edit_graph', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(GraphUpdate, self).get_context_data(**kwargs)
        context['title'] = _('Graph')
        return context


class GraphSelectorUpdate(LoginRequiredMixin, GraphUserGroupRequiredMixin, UpdateView):
    model = GraphSelector
    form_class = GraphSelectorForm
    template_name = "generic/edit_template.html"

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(GraphSelectorUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(GraphSelectorUpdate, self).form_invalid(form)

    def get_success_url(self):
        return reverse('edit_graph_selector', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(GraphSelectorUpdate, self).get_context_data(**kwargs)
        context['title'] = _('Graph Selector')
        return context


class TypeUpdate(LoginRequiredMixin, GraphUserGroupRequiredMixin, UpdateView):
    model = Type
    form_class = TypeForm
    template_name = "generic/edit_template.html"

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(TypeUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(TypeUpdate, self).form_invalid(form)

    def get_success_url(self):
        return reverse('edit_type', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(TypeUpdate, self).get_context_data(**kwargs)
        context['title'] = _('Type')
        return context


class InstanceUpdate(LoginRequiredMixin, GraphUserGroupRequiredMixin, UpdateView):
    model = Instance
    form_class = InstanceForm
    template_name = "generic/edit_template.html"

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(InstanceUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(InstanceUpdate, self).form_invalid(form)

    def get_success_url(self):
        return reverse('edit_instance', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(InstanceUpdate, self).get_context_data(**kwargs)
        context['title'] = _('Instance')
        return context


# Generic Delete views

def delete_redirect(request, name, pk):
    return redirect(('delete_' + name), pk)


class GraphDelete(LoginRequiredMixin, GraphUserGroupRequiredMixin, DeleteView):
    template_name = "generic/delete_template.html"
    model = Graph
    success_url = reverse_lazy('list_graph')

    def get_context_data(self, **kwargs):
        context = super(GraphDelete, self).get_context_data(**kwargs)
        context['title'] = _("Graph")
        return context


class GraphSelectorDelete(LoginRequiredMixin, GraphUserGroupRequiredMixin, DeleteView):
    template_name = "generic/delete_template.html"
    model = GraphSelector
    success_url = reverse_lazy('list_graph_selector')

    def get_context_data(self, **kwargs):
        context = super(GraphSelectorDelete, self).get_context_data(**kwargs)
        context['title'] = _("Graph Selector")
        return context


class TypeDelete(LoginRequiredMixin, GraphUserGroupRequiredMixin, DeleteView):
    template_name = "generic/delete_template.html"
    model = Type
    success_url = reverse_lazy('list_type')

    def get_context_data(self, **kwargs):
        context = super(TypeDelete, self).get_context_data(**kwargs)
        context['title'] = _("Type")
        return context


class InstanceDelete(LoginRequiredMixin, GraphUserGroupRequiredMixin, DeleteView):
    template_name = "generic/delete_template.html"
    model = Instance
    success_url = reverse_lazy('list_instance')

    def get_context_data(self, **kwargs):
        context = super(InstanceDelete, self).get_context_data(**kwargs)
        context['title'] = _("Instance")
        return context

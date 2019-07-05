from django import forms
from django.forms import TextInput
from django.utils.translation import gettext as _

from .models import *


class GraphForm(forms.ModelForm):
    class Meta:
        model = Graph
        fields = ('name', 'title', 'dashboard', 'public', 'selector')


class GraphSelectorForm(forms.ModelForm):
    class Meta:
        model = GraphSelector
        fields = ('name', 'title', 'type', 'instance', 'color')
        widgets = {'color': TextInput(attrs={'type': 'color'})}


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ('name', 'description', 'unit')


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = ('name', 'description')

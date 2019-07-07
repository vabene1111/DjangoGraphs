from django import template

from DjangoGraphs.models import Settings

register = template.Library()


@register.simple_tag
def get_title():
    return Settings.objects.get(pk=1).title

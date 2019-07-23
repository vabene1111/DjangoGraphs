from django.utils.translation import gettext as _
from rest_framework import serializers

from DjangoGraphs.models import DataEntry, Graph


class DataEntrySerializer(serializers.ModelSerializer):
    view_name = 'api_entry'

    class Meta:
        model = DataEntry
        fields = ('type', 'instance', 'value', 'timestamp')
        extra_kwargs = {
            'url': {'view_name': 'api_entry'}
        }


class GraphDataSerializer(serializers.Serializer):
    graph = serializers.IntegerField()
    limit = serializers.IntegerField()

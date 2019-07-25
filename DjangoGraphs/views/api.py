import datetime
import itertools
import json

import django
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncHour
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django.utils.translation import gettext as _

from ..serializers import *


class DataEntrySet(viewsets.ModelViewSet):
    """
    API endpoint that allows data entries to be viewed or edited.
    """
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer

    permission_classes = (permissions.IsAuthenticated,)


class GraphDataView(APIView):
    """
    Retrieve Graph Data
    """
    serializer_class = GraphDataSerializer

    def get(self, request):
        results = request.query_params
        if not isinstance(int(results['graph']), int):
            return Response({'err': '0', 'msg': 'Incorrect type for graph parameter'})

        try:
            graph = Graph.objects.get(pk=int(results['graph']))
        except Graph.DoesNotExist:
            return Response({'err': '1', 'msg': 'No graph with given id'})

        if not request.user.is_authenticated and not graph.public:
            return Response({'err': '2', 'msg': 'This data cannot be viewed without authentication'})

        data = []

        for s in graph.selector.all():
            arr = []
            entries = DataEntry.objects.annotate(hour=TruncHour('timestamp')).filter(type=s.type, instance=s.instance).order_by('timestamp').all()

            last_hour = entries[0].timestamp.hour

            for e in entries:
                if e.timestamp.hour != last_hour:
                    arr.append({'date': e.timestamp, 'value': round(e.value, 2)})
                    last_hour = e.timestamp.hour

            data.append(arr)

        return Response(data)

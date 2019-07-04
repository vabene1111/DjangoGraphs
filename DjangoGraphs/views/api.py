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

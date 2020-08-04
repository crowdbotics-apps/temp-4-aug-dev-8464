from rest_framework import authentication
from homekjhgjkhkjh.models import Hgjh
from .serializers import HgjhSerializer
from rest_framework import viewsets


class HgjhViewSet(viewsets.ModelViewSet):
    serializer_class = HgjhSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hgjh.objects.all()

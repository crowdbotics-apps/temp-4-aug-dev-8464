from rest_framework import authentication
from jhgjhg.models import JHgjhg
from .serializers import JHgjhgSerializer
from rest_framework import viewsets


class JHgjhgViewSet(viewsets.ModelViewSet):
    serializer_class = JHgjhgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = JHgjhg.objects.all()

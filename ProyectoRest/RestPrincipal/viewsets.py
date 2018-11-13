from rest_framework import generics
from rest_framework import viewsets

from .serializers import SolicitudSerializer
from Principal.models import Solicitud

class SolicitudViewSet(viewsets.ModelViewSet):
	queryset = Solicitud.objects.all()
	serializer_class = SolicitudSerializer
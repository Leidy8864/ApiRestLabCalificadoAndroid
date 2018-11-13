from rest_framework import serializers

from Principal.models import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
	class Meta:
		model= Solicitud
		fields= ('correo', 'tipo', 'motivo', 'imagen')
from django.db import models

class Solicitud(models.Model):
	codigo 	= models.AutoField(primary_key=True)
	correo 	= models.EmailField(max_length=254)
	tipo 	= models.CharField(max_length=254)
	motivo 	= models.CharField(max_length=254)
	imagen = models.FileField(default=None, blank=True, upload_to='storage/images/', null=True)

	def __unicode__(self):
		return self.codigo
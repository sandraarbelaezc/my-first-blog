from django.db import models #Agrega algo de otros archivos
from django.utils import timezone


class Post(models.Model):	#define el objeto
	author = models.ForeignKey('auth.User')	# Propiedades
	tittle = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	pubished_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):	#Métodos
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.tittle

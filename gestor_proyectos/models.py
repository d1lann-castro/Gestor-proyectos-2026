from django.db import models


class Proyecto(models.Model):
    """Representa un proyecto registrado en el gestor."""

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    duracion = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

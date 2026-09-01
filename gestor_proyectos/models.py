from django.db import models

class Proyecto(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    nombre = models.CharField(max_length=100) #Un campo de texto osea un (Varchar)
    descripcion = models.TextField() #Campo de texto blanco
    duracion = models.IntegerField() #Campo numerico entero
    imagen = models.ImageField(upload_to='img/', default='img/logo.png') #Campo de imagen

    def __str__(self):
        return self.nombre

    

class Tarea(models.Model):
    '''
    Modelo que representa una tarea de un proyecto
    '''

    PRIORIDAD_CHOICES= [
        ('BAJA', 'Baja'), 
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    ]

    ESTADO_CHOICES=[
        ('PENDINTE', 'Pendiente'), 
        ('EN_PROGRESO', 'En progreso'),
        ('COMPLETADA', 'Completada')
    ]

    #Relacion 1 a muchos: Un proyecto tiene muchas tareas
    proyecto= models.ForeignKey(
        Proyecto,
        on_delete= models.CASCADE,
        related_name= 'tareas'
    )
    titulo = models.CharField(max_length=50)
    prioridad= models.CharField(
        max_length=5,
        choices= PRIORIDAD_CHOICES,
        default='MEDIA'
    )

    estado= models.CharField(
        max_length=11,
        choices= ESTADO_CHOICES,
        default='PENDIENTE',
    )

    def __str__(self):
        return self.titulo + "(" + self.proyecto.nombre + ")"
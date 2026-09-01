from django.contrib import admin
from .models import Proyecto,Tarea


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre", "descripcion")

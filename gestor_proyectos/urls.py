from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("proyectos/", views.mostrar_proyectos, name="proyectos"),
    path("nuevos-registros/", views.nuevos_registros, name="nuevos_registros"),
    path("proyectos/nuevo/", views.nuevo_proyecto, name="nuevo_proyecto"),
    path("proyectos/crear/", views.crear_proyecto, name="crear_proyecto"),
    path("proyectos/<int:id>/", views.ver_proyecto, name="ver_proyecto"),
    path("proyectos/<int:id>/eliminar/", views.eliminar_proyecto, name="eliminar_proyecto"),
    path('proyectos/nuevo/', views.nuevo_proyecto, name='nuevo-proyecto'),
    #path('proyectos/crear_proyecto/', views.crear_proyecto, name='crear_proyecto')
]

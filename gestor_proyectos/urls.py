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
    path('proyectos/<int:id>/editar/', views.editar_proyecto, name= 'editar_proyecto'),
    path('proyectos/<int:proyecto_id>/tareas/nueva/', views.crear_tarea, name='crear_tarea')
    
]  
    #path('proyectos/crear_proyecto/', views.crear_proyecto, name='crear_proyecto'

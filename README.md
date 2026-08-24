# Proyecto Gestor

## Ejecutar

1. Crear/activar un entorno virtual.
2. Instalar dependencias:
   pip install -r requirements.txt
3. Aplicar migraciones:
   python manage.py migrate
4. Ejecutar:
   python manage.py runserver

## Rutas principales

- /                         -> inicio
- /proyectos/               -> lista de proyectos
- /proyectos/nuevo/         -> formulario de creación
- /proyectos/crear/         -> procesamiento POST del formulario
- /proyectos/<id>/          -> detalle
- /proyectos/<id>/eliminar/ -> eliminación por POST
- /nuevos-registros/        -> carga registros de ejemplo sin duplicarlos

La carpeta venv original no se incluye; se recomienda crear el entorno virtual localmente con la versión de Python compatible e instalar requirements.txt.

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Proyecto, Tarea


def home(request):
    return render(request, "home.html")


def mostrar_proyectos(request):
    proyectos = Proyecto.objects.all().order_by("-id")
    return render(request, "proyectos.html", {"proyectos": proyectos})


def nuevos_registros(request):
    ejemplos = [
        {
            "nombre": "Aplicacion bancaria",
            "descripcion": "Aplicacion web para gestionar cuentas bancarias",
            "duracion": 1000,
        },
        {
            "nombre": "Aplicacion mensajeria",
            "descripcion": "Aplicacion para enviar mensajes de texto",
            "duracion": 100,
        },
    ]

    for datos in ejemplos:
        Proyecto.objects.get_or_create(
            nombre=datos["nombre"],
            defaults={
                "descripcion": datos["descripcion"],
                "duracion": datos["duracion"],
            },
        )

    return redirect("proyectos")


def ver_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    print(proyecto.tareas)
    return render(request, "detalle_proyecto.html", {"proyecto": proyecto})


def nuevo_proyecto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')

        if nombre and descripcion and duracion:
            proyecto = Proyecto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                duracion=duracion,
            )
            proyecto.save()
            return redirect('proyectos')

    return render(request, 'nuevo-proyecto.html')


def crear_proyecto(request):
    if request.method != "POST":
        return redirect("nuevo_proyecto")

    nombre = request.POST.get("nombre", "").strip()
    descripcion = request.POST.get("descripcion", "").strip()
    duracion_raw = request.POST.get("duracion", "").strip()

    errores = []

    if not nombre:
        errores.append("El nombre del proyecto es obligatorio.")

    if not descripcion:
        errores.append("La descripción del proyecto es obligatoria.")

    try:
        duracion = int(duracion_raw)
        if duracion <= 0:
            errores.append("La duración debe ser mayor que 0.")
    except (TypeError, ValueError):
        duracion = None
        errores.append("La duración debe ser un número entero mayor que 0.")

    if errores:
        return render(
            request,
            "nuevo-proyecto.html",
            {
                "errores": errores,
                "nombre": nombre,
                "descripcion": descripcion,
                "duracion": duracion_raw,
            },
        )

    Proyecto.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        duracion=duracion,
    )

    messages.success(request, "El proyecto se creó correctamente.")
    return redirect("proyectos")

def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id= id)
    proyecto.delete()
    return redirect("proyectos")


def editar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id= id )


    if request.method == 'POST':
        nombre = request.POST.get('nombre').strip()
        descripcion = request.POST.get('descripcion')
        duarcion = request.POST.get('duarcion')


        if nombre and descripcion and duarcion:
            proyecto.nombre= nombre
            proyecto.descripcion= descripcion
            proyecto.duarcion= int(duarcion)
            proyecto.save()


            return redirect('ver_proyecto', id=proyecto.id)        


    return render (request, 'editar_proyecto.html', {'proyecto': proyecto})

def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == "POST":
        titulo = request.POST.get('titulo').strip()
        prioridad= request.POST.get('prioridad')
        estado= request.POST.get('estado')

        if titulo:
            tarea = Tarea(
                titulo=titulo, 
                prioridad=prioridad, 
                estado=estado)
            tarea.save()

            return redirect('ver_proyecto', id=proyecto_id)

    datos = {
        'proyecto': proyecto,
        'prioridad_choices': Tarea.PRIORIDAD_CHOICES,
        'estado_choices': Tarea.ESTADO_CHOICES
    }

    return render(request, 'crear_tarea.html', datos)

def avanzar_estado_tarea (request,id):
    tarea = get_object_or_404(Tarea, id=id)

    if tarea.estado == "PENDIENTE":
        tarea.estado == "EN_PROGRESO"
        tarea.save()
    elif tarea.estado == "EN_PROGRESO":
        tarea.estado = "COMPLETADO"
        tarea.save()

    return redirect('ver_proyecto', id = tarea.proyecto.id)


        

 
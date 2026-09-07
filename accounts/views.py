from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User, Group

def registro(request):
    datos= ''
    errors = []

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2= request.POST.get('password2')

        datos = request.POST

        #validaccion basica 

        if password1 != password2:
            errors.append('Las contraseñas no coninciden')

        if User.objects.filter(username= username).exists():
            errors.append('El nombre de usuario ya existe')

        if User.objects.filter(email= email).exists():
            errors.append('El correo electronico ya esta registrado')

        if not errors:
            #create_user hata la contrseña automaticamente
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            return redirect ('home')
    return render(request, 'registro.html', {'errors': errors, 'datos': datos})

def grupos(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre').strip()
        if nombre and not Group.objects.filter(name = nombre).exists():
            return redirect('grupos')
        return redirect ('grupos')
    grupos = Group.objects.all()
    return render(request, 'grupos.html', {'grupos': grupos})
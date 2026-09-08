from django.urls import path
from django.contrib.auth import views as auth_views
from .views import registro, grupos, editar_grupo, eliminar_grupo

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('grupos/', grupos, name='grupos'),
    path('grupos/editar/<int:group_id>/', editar_grupo, name='editar_grupo'),
    path('grupos/eliminar/<int:group_id>/', eliminar_grupo, name='eliminar_grupo'),
]
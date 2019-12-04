from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_trabajador, name='lista_trabajador'),
    path('agregar', views.agregar_trabajador, name='agregar_trabajador'),
    path('buscar', views.buscar_trabajador, name='buscar_trabajador'),
    path('eliminar/<int:id>', views.eliminar_trabajador, name='eliminar_trabajador'),
    path('modificar/<int:id>', views.modificar_trabajador, name='modificar_trabajador'),
]
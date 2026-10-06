from django.urls import path
from . import views

urlpatterns = [
    path("", views.indice, name="indice"),
    path("acerca/", views.acerca, name="acerca"),
    path("bienvenido/", views.bienvenido, name="bienvenido"),
    path("contacto/", views.contacto, name="contacto"),
    path("exito/", views.exito, name="exito"),
    path("flan/<uuid:flan_uuid>/", views.detalle_flan, name="detalle_flan"),
]

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from . import models
from . import forms


def indice(request):
    contexto = {"productos": models.Flan.objects.filter(is_private=False)}
    return render(request, "index.html", contexto)


def acerca(request):
    return render(request, "about.html")


@login_required
def bienvenido(request):
    contexto = {"productos": models.Flan.objects.filter(is_private=True)}
    return render(request, "welcome.html", contexto)


def contacto(request):
    # GUARDAR INFORMACIÓN
    formulario = forms.ContactFormModelForm
    if request.method == "POST":
        form = formulario(request.POST)
        if form.is_valid():
            # guardar la respuesta del usuario en la base de datos
            """
            INSERT INTO ContactForm
            VALUES(...,...,...);
            """
            models.ContactForm.objects.create(**form.cleaned_data)

            return redirect("exito")

    # pidiendo obtener alguna información
    elif request.method == "GET":
        form = formulario()
    contexto = {"form": form}
    return render(request, "contactus.html", contexto)


def exito(request):
    return render(request, "success.html")


def detalle_flan(request, flan_uuid):
    flan = get_object_or_404(models.Flan, flan_uuid=flan_uuid)
    if flan.is_private and not request.user.is_authenticated:
        return redirect_to_login(request.get_full_path())
    return render(request, "flan_detalle.html", {"flan": flan})


@require_POST
def logout_view(request):
    logout(request)
    return render(request, "registration/sesion_cerrada.html")

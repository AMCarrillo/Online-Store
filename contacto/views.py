from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()
    return render(request, "contacto/contacto.html", {"mi_formulario":formulario_contacto})
    
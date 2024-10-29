# En voluntarios/views.py
from django.shortcuts import render, get_object_or_404
from .models import Oportunidad, Contacto

def index(request):
    oportunidades = Oportunidad.objects.all()

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Guardar en la base de datos
        contacto = Contacto(nombre=nombre, email=email, mensaje=mensaje)
        contacto.save()

    return render(request, 'index.html', {'oportunidades': oportunidades})


# Vista de detalles de una oportunidad
def oportunidad_detalle(request, id):
    oportunidad = get_object_or_404(Oportunidad, id=id)
    return render(request, 'oportunidad_detalle.html', {'oportunidad': oportunidad})
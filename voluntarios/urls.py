# En voluntarios/urls.py
from django.urls import path
from .views import index, oportunidad_detalle

urlpatterns = [
    path('', index, name='inicio'),  # Esta será la única ruta
    path('oportunidad/<int:id>/', oportunidad_detalle, name='oportunidad_detalle'),  # Nueva ruta para los detalles
]

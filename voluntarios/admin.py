# En voluntarios/admin.py
from django.contrib import admin
from .models import Oportunidad, Contacto

admin.site.register(Oportunidad)
admin.site.register(Contacto)
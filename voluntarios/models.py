from django.db import models

class Oportunidad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=100)
    fecha = models.DateField()
    requisitos = models.TextField(null=True)  # Asegúrate de tener este campo
    contacto = models.CharField(max_length=100, null=True)  # Cambia a nullable
    imagen = models.ImageField(upload_to='voluntariados/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.email})"
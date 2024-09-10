from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Mensajes (models.Model):
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"De: {self.remitente} - Para {self.destinatario}"
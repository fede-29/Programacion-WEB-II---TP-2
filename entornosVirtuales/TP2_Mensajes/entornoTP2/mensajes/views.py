from django.shortcuts import get_object_or_404, redirect, render
from .models import Mensajes

# Create your views here.
def enviar_mensaje(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        remitente = request.POST.get('remitente')
        destinatario = request.POST.get('destinatario')

        Mensajes.objects.create(
            mensaje = mensaje,
            remitente = remitente,
            destinatario = destinatario
        )
    
    return render (request, 'enviar_mensaje.html')
        
def ver_mensaje(request):
    mensajes = Mensajes.objects.all()
    
    return render(request, 'ver_mensaje.html', {'mensajes': mensajes})

def eliminar_mensaje (request, mensaje_id):
    mensaje = get_object_or_404(Mensajes, id=mensaje_id)
    if request.method == 'POST':
        mensaje.delete()
        return redirect ('ver_mensaje')
    return render(request, 'eliminar_mensaje.html', {'mensaje':mensaje})

def principal (request):
    return render (request, 'base.html')
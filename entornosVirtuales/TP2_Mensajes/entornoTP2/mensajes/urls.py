from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_mensaje, name ='enviar_mensaje'),
    path('recibido/',views.ver_mensaje, name='ver_mensaje'),
    path('eliminar_mensaje/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
    path('', views.principal, name='principal'),
]
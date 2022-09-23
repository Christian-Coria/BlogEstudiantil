
from django.urls import path
from integrador.views import ProyectoIntegrador, CrearFormato


urlpatterns = [
    
    path('proyecto',ProyectoIntegrador.as_view(), name="proyecto"),  
    path('crear-formato' , CrearFormato.as_view(), name='crear_formato'),        
    #path('crear-album' , CrearAlbum.as_view(), name='crear_album'),

]
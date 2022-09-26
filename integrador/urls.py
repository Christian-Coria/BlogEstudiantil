
from django.urls import path
from integrador.views import ProyectoIntegrador#, CrearGenero, MostrarInterprete, EliminarGenero, EditarGenero, MostrarGenero ,ListarGenero


urlpatterns = [
    
    path('proyecto',ProyectoIntegrador.as_view(), name="proyecto"),         
   
    

    # path('crear-album' , CrearAlbum.as_view(), name='crear_album'),
    # path('eliminar-album/<int:pk>' , EliminarAlbum.as_view(), name='eliminar_album'),
    # path('editar-album/<int:pk>' , EditarAlbum.as_view(), name='editar_album'),
    # path('listar-album' , ListarAlbum.as_view(), name='listar_album'),
    # path('mostrar-album/<int:pk>/' , MostrarAlbum.as_view(), name='mostrar_album'),

    

]

from django.urls import path
from integrador.views import ProyectoIntegrador#, CrearGenero, MostrarInterprete, EliminarGenero, EditarGenero, MostrarGenero ,ListarGenero


urlpatterns = [
    
    path('proyecto',ProyectoIntegrador.as_view(), name="proyecto"),         
   
    

    # path('crear-album' , CrearAlbum.as_view(), name='crear_album'),
    # path('eliminar-album/<int:pk>' , EliminarAlbum.as_view(), name='eliminar_album'),
    # path('editar-album/<int:pk>' , EditarAlbum.as_view(), name='editar_album'),
    # path('listar-album' , ListarAlbum.as_view(), name='listar_album'),
    # path('mostrar-album/<int:pk>/' , MostrarAlbum.as_view(), name='mostrar_album'),

    path('crear-tema' , CrearTema.as_view(), name='crear_tema'),
    path('eliminar-tema/<int:pk>' , EliminarTema.as_view(), name='eliminar_tema'),
    path('editar-tema/<int:pk>' , EditarTema.as_view(), name='editar_tema'),
    path('listar-tema' , ListarTema.as_view(), name='listar_tema'),
    path('mostrar-tema/<int:pk>/' , MostrarTema.as_view(), name='mostrar_tema'),

    path('crear-interprete' , CrearInterprete.as_view(), name='crear_interprete'),
    path('eliminar-interprete/<int:pk>' , EliminarInterprete.as_view(), name='eliminar_interprete'),
    path('editar-interprete/<int:pk>' , EditarInterprete.as_view(), name='editar_interprete'),
    path('listar-interprete' , ListarInterprete.as_view(), name='listar_interprete'),
    path('mostrar-interprete/<int:pk>/' , MostrarInterprete.as_view(), name='mostrar_interprete'),
    

]
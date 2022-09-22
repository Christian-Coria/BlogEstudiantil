
from django.urls import path
from integrador.views import ProyectoIntegrador


urlpatterns = [
    
    path('proyecto',ProyectoIntegrador.as_view(), name="proyecto"),  


]
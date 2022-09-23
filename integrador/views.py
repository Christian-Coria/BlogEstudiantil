from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from integrador.models import  Formato

class ProyectoIntegrador(TemplateView):
    template_name = "integrador/proyecto.html"


class CrearFormato(CreateView):
    model = Formato
    template_name = "integrador/crear_formato.html"
    success_url = 'proyecto'
    fields = ['tipo']

# class CrearAlbum(CreateView):        # DESCOMENTAR HE IMPORTAR AL CREAR LAS DEMAS TABLAS!!!!
#     model = Album
#     template_name = "crear_album.html"
#     success_url = 'proyecto'
#     fields = ['nombre','interprete','genero','cant_temas', 'discografica', 'formato', 'fec_lanzamiento', 'precio', 'cantidad', 'caratula']


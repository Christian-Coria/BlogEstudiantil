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

def buscar_album(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_album_list = Album.objects.filter(Q(nombre__icontains=q)).order_by('nombre',
        Q(genero__icontains=q)).order_by('genero'), (Q(interprete__icontains=q)).order_by('interprete')
    else:
        all_album_list = Album.objects.all().order_by('nombre')
        all_album_list = Album.objects.all().order_by('genero')
        all_album_list = Album.objects.all().order_by('interprete')

    return render(request, 'buscar_album.html', {"album":all_album_list})
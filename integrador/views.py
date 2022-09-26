from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from integrador.models import  Formato, Album, Discografica, Genero, Interprete, Tema

class ProyectoIntegrador(TemplateView):
    template_name = "integrador/proyecto.html"


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


class CrearAlbum(CreateView):        
    model = Album
    template_name = "integrador/crear_album.html"
    success_url = 'proyecto'
    fields = ['nombre','interprete','genero','cant_temas', 'discografica', 'formato', 'fec_lanzamiento', 'precio', 'cantidad']


class ListarAlbum(ListView):
    model = Album
    template_name = "integrador/listar_album.html"


class EditarAlbum(UpdateView):
    model = Album
    template_name ='integrador/editar_album.html'
    success_url = reverse_lazy('listar_albums')
    fields = ['nombre','interprete','genero','cant_temas', 'discografica', 'formato', 'fec_lanzamiento', 'precio', 'cantidad'] 


class EliminarAlbum(DeleteView):
    model = Album
    template_name = "integrador/eliminar_album.html"
    success_url = reverse_lazy('listar_album')


class MostrarAlbum(DetailView):
    model = Album
    template_name = 'integrador/mostrar_album.html'

class CrearFormato(CreateView):
    pass


class ListarFormato(ListView):
    pass

class EditarFormato(UpdateView):
    pass


class EliminarFormato(DeleteView):
    pass

class MostrarFormato(DetailView):
    pass

class ListarTema(ListView):
    model = Tema
    template_name = "integrador/listar_tema.html"


class EditarTema(UpdateView):
    model = Tema
    template_name ='integrador/editar_tema.html'
    success_url = reverse_lazy('listar_tema')
    fields = ['titulo','duracion','autor','compositor', 'cod_album', 'interprete'] 


class EliminarTema(DeleteView):
    model = Tema
    template_name = "integrador/eliminar_tema.html"
    success_url = reverse_lazy('listar_tema')


class MostrarTema(DetailView):
    model = Tema
    template_name = 'mostrar_tema.html'


class CrearInterprete(CreateView):        
    model = Interprete
    template_name = "integrador/crear_interprete.html"
    success_url = 'proyecto'
    fields = ['nombre', 'foto']


class ListarInterprete(ListView):
    model = Interprete
    template_name = "integrador/listar_interprete.html"


class EditarInterprete(UpdateView):
    model = Interprete
    template_name ='integrador/editar_interprete.html'
    success_url = reverse_lazy('listar_interprete')
    fields = ['nombre', 'foto'] 


class EliminarInterprete(DeleteView):
    model = Interprete
    template_name = "integrador/eliminar_interprete.html"
    success_url = reverse_lazy('listar_interprete')


class MostrarInterprete(DetailView):
    model = Interprete
    template_name = 'integrador/mostrar_interprete.html'



class CrearGenero(CreateView):        
    pass


class ListarGenero(ListView):
    pass


class EditarGenero(UpdateView):
    pass 


class EliminarGenero(DeleteView):
    pass

class MostrarGenero(DetailView):
    pass


class CrearDiscografica(CreateView):        
    pass

class ListarDiscografica(ListView):
    pass


class EditarDiscografica(UpdateView):
    pass


class EliminarDiscografica(DeleteView):
    pass


class MostrarDiscografica(DetailView):
    pass

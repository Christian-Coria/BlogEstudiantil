
from django.shortcuts import render
from django.views.generic import TemplateView



def home(request):
    return render(request,'index.html')


class About(TemplateView):
    template_name = "about.html"


class Contacto(TemplateView):
    template_name = "contacto.html"
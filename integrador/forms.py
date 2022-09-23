from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormatoCreationForm(forms.Form):
    tipo = forms.CharField(max_length=40)

# clase y metodo str a crear y completar por mateo
class CreationForm(forms.Form):
    pass



# clase y metodo str a crear y completar por mateo
class CreationForm(forms.Form):
    pass

# clase y metodo str a crear y completar por joaquin
class CreationForm(forms.Form):
    pass


# clase y metodo str a crear y completar por joaquin
class CreationForm(forms.Form):
    pass  

# class AlbumCreationForm(forms.Form):                     # DESCOMENTAR  HE IMPORTAR AL CREAR LAS DEMAS TABLAS!!!!

#     nombre = forms.CharField(label='Nombre', max_length=30, required=False)
#     interprete = forms.ForeignKey(Interprete, on_delete=forms.DO_NOTHING)
#     genero = forms.ForeignKey(Genero, on_delete=forms.DO_NOTHING)
#     cant_temas = forms.CharField(label='Cantidad de Temas', widget=forms.PasswordInput,required=False)
#     discografica = forms.ForeignKey(Discografica, on_delete=forms.DO_NOTHING)
#     fec_lanzamiento = forms.CharField(max_length=40)
#     precio = forms.IntegerField()    
#     cantidad = forms.IntegerField()
#     caratula = forms.ImageField(required=False)
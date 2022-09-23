from django.db import models

# Create your models here.



class Formato(models.Model):
     tipo = models.CharField(max_length=40)

def __str__(self):
    return f'Clase {self.tipo}'


# clase y metodo str a crear y completar por mateo
class Tema(models.Model):
    pass



# clase y metodo str a crear y completar por mateo
class Interprete(models.Model):
    pass

# clase y metodo str a crear y completar por joaquin
class Genero(models.Model):
    pass


# clase y metodo str a crear y completar por joaquin
class Discografia(models.Model):
    pass  


# para ordenar la lista 
# def __unicode__(self): 
#         return self.nombre_deporte_es

#     class Meta:
#         ordering = ['-nombre_deporte_es'] # Nota el guión

#se crea la clase Album y se coloca al final ya que de esa forma heredara de las anteriores clases   DESCOMENTAR AL CREAR LAS DEMAS TABLAS!!!!!
class Album(models.Model):
    pass
#     nombre = models.CharField(max_length=255)
#     interprete = models.ForeignKey(Interprete,null=True, on_delete=models.CASCADE)
#     genero = models.ForeignKey(Genero,null=True, on_delete=models.CASCADE)
#     cant_temas = models.IntegerField()
#     discografica = models.ForeignKey(Discografica,null=True, on_delete=models.CASCADE)
#     formato = models.ForeignKey(Formato,null=True, on_delete=models.CASCADE)
#     fec_lanzamiento = models.CharField(max_length=40)
#     precio = models.IntegerField()
#     cantidad = models.IntegerField()
#     imagen = models.ImageField(upload_to="caratula", null=True, blank=True)

    
#   def __str__(self):
#         return f'Album: {self.id} {self.nombre} {self.genero} {self.cant_temas} {self.discografica} {self.formato} {self.fec_lanzamiento} {self.precio} {self.cantidad} '
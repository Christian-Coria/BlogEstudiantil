from django.db import models


class Formato(models.Model):
    pass

class Interprete(models.Model):
    pass
    
class Genero(models.Model):
    pass

class Discografica(models.Model):
    pass

# class Album(models.Model):

#     nombre = models.CharField(max_length=255)
#     interprete = models.ForeignKey(Interprete,null=True, on_delete=models.CASCADE)
#     genero = models.ForeignKey(Genero,null=True, on_delete=models.CASCADE)
#     cant_temas = models.CharField(max_length=40)
#     discografica = models.ForeignKey(Discografica,null=True, on_delete=models.CASCADE)
#     formato = models.ForeignKey(Formato,null=True, on_delete=models.CASCADE)
#     fec_lanzamiento = models.CharField(max_length=40)
#     precio = models.IntegerField()
#     cantidad = models.IntegerField()
#     imagen = models.ImageField(upload_to="caratula", null=True, blank=True)
  
#     def __str__(self):
#        return f'{self.nombre}'


class Tema(models.Model):
   pass 
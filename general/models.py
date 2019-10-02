from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.template.defaultfilters import slugify
# Create your models here.
class Categoria(models.Model):
    """Model definition for Categorias."""

    nombre = models.CharField(max_length=50)
    


    class Meta:
        """Meta definition for Categorias."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return u'/categoria/%d' % self.id 

#class Images(models.Model):
  #  proyecto=models.ForeignKey(Proyecto,on_delete= models.PROTECT)    
   # image = models.ImageField(upload_to='imagenes',
    #                          null=False)

class Proyecto(models.Model):
    """Model definition for Proyecto."""

    nombre= models.CharField(max_length=50)
    descripcion= models.TextField(blank=True)
    fecha= models.DateField()
    imagen=models.ImageField(upload_to='fotos',null=True)
    categoria=models.ForeignKey(Categoria,on_delete= models.PROTECT)
    class Meta:
        """Meta definition for Proyecto."""

        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    
    
    def get_absolute_url(self):
        return u'/categoria/faturas/%d' % self.id 

    def __str__(self):
        return self.nombre

    






from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="Project")# Guarda dentro de la carpeta Project en media
    link= models.URLField(null=True, blank=True, verbose_name='Direccion Web')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")


    def __str__(self):
        return self.title
    
    # Con meta defino para que los proyectos se muestren en el panel de administrador en Español
    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        
        # Ordenar los proyectos, que se muestren los mas recientes primero
        ordering= ["-created"] 
    
    




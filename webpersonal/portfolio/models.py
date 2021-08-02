from django.db import models

"""
models.Model representa una tabla dentro de la BD
"""

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    url = models.URLField(null = True, blank = True, default = "null")

    """
    Para que Django detecte el nombre en español del modelo de Poject creamos una clase meta
    """
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
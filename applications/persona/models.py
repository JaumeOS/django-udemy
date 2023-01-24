from django.db import models
from ckeditor.fields import RichTextField
from applications.departamento.models import Departamento


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.habilidad


class Persona(models.Model):
    JOB_CHOICES = (
        ('0', 'INFORMATICO'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'GEOLOGO'),
    )

    first_name = models.CharField('Nombre', max_length=50)
    surnames = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Empleados'
        ordering = ['-first_name']
        unique_together = ('first_name', 'surnames')

    def __str__(self):
        return self.first_name + '-' + self.surnames

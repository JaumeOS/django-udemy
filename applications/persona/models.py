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
    full_name = models.CharField(
        'Nombre completo',
        max_length=120,
        blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    habilidades.short_description = "Habilidades"

    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Empleados'
        ordering = ['-first_name']
        unique_together = ('first_name', 'surnames')

    # def show_habilidades(self):
    #     return ', '.join([h.habilidades for h in self.objects.all()])

    def __str__(self):
        return self.first_name + '-' + self.surnames

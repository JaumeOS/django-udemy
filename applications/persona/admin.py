from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Habilidades)


class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'surnames',
        'departamento',
        'job',
        'full_name',
    )

    def full_name(self, obj):
        # operación
        print(obj.first_name)
        return obj.first_name + ' ' + obj.surnames

    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades')

    # para campos m2m
    filter_horizontal = ('habilidades',)


admin.site.register(Persona, PersonaAdmin)

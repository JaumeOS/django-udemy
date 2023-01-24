from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Persona


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Persona
    context_object_name = 'lista'


class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Persona.objects.filter(
            departamento__name=area
        )
        return lista


class FormKword(ListView):
    template_name = "persona/form_kword.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*********************')
        #                                 id="kword" from .html
        palabra_clave = self.request.GET.get("kword", '')
        lista = Persona.objects.filter(
            surnames=palabra_clave
        )

        print('lista resultados: ', lista)
        return lista

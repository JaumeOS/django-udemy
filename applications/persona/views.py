from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    TemplateView, 
    UpdateView, 
    DeleteView
)
from django.core.paginator import Paginator

from .models import Persona
from .forms import *

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    model = Persona
    context_object_name = 'lista'


class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'lista'

    def get_queryset(self):
        area = self.kwargs['shor_name']
        lista = Persona.objects.filter(
            departamento__shor_name=area
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


class FormKwordPaginate(ListView):
    template_name = "persona/form_kword_paginate.html"

    # nom que reb l'objecte object_list
    context_object_name = 'empleados'
    paginate_by = 1

    def get_n_pagina(request):
        persona_list = Persona.objects.all
        paginator = Paginator(persona_list, 4)

        n_pagina = request.GET.get("page", '1')
        page_obj = paginator.get_page(n_pagina)
        return page_obj

    paginate_by = get_n_pagina

    def get_queryset(self):
        lista = Persona.objects.all()
        return lista


class ListaHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_empleado = self.request.GET.get("idempleado", '1')
        empleado = Persona.objects.get(id=id_empleado)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "persona/detail_view.html"


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class PersonaCreateView(CreateView):
    model = Persona
    template_name = "persona/add.html"
    # fields = ('__all__')
    fields = [
        'first_name',
        'surnames',
        'departamento',
        'job',
        'habilidades',
    ]

    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        # commit=False crea la instancia sin actualizar el valor
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.surnames
        # .save() actualiza el valor nuevo de esa instancia de empleado
        empleado.save()
        print(empleado)
        return super(PersonaCreateView, self).form_valid(form)


class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'surnames',
        'departamento',
        'job',
        'habilidades',
    ]
        
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args: str, **kwargs) :
        print('**************POST*****************')
        print(request.POST)
        print(request.POST['habilidades'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('**************FORM*****************')
        return super(PersonaUpdateView, self).form_valid(form)


class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = "persona/delete.html"

    success_url = reverse_lazy('persona_app:correcto')


class PruebPersonaCreateView(CreateView):
    model = Persona
    template_name = "persoa/add.html"
    success_url = reverse_lazy('persona_app:correcto')
    form_class = EmpleadoForm
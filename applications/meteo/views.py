from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
class MeteoView(TemplateView):
    template_name = 'meteo/meteo.html'

class PruebaListView(ListView):
    template_name = 'meteo/lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'

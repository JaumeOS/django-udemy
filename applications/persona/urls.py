from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [

    path('listar-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<shor_name>', views.ListByAreaEmpleados.as_view()),
    path('form_kword/', views.FormKword.as_view()),
    path('form_kword_paginate/', views.FormKwordPaginate.as_view()),
    path('habilidades/', views.ListaHabilidadesEmpleado.as_view()),
    path('detalle/<pk>', views.EmpleadoDetailView.as_view()),
    path('add/', views.PersonaCreateView.as_view()),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
    ),
    path(
        'update/<pk>',
        views.PersonaUpdateView.as_view(),
        name='update'
    ),
    path(
        'delete/<pk>',
        views.PersonaDeleteView.as_view(),
        name='delete'
    ),
]

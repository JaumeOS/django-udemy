from django.urls import path
from . import views

urlpatterns = [
    path('listar-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<shorname>', views.ListByAreaEmpleados.as_view()),
    path('form_kword', views.FormKword.as_view()),
]


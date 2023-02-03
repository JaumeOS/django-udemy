from django.urls import path
from . import views

urlpatterns = [
    path('meteo/', views.MeteoView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('prueba/', views.PruebaView.as_view()),
]

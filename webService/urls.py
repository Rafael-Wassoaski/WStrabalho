from django.contrib import admin
from django.urls import path, include
from . import views




urlpatterns = [
    path('randomvalue/', views.sorteio, name = 'sorteio'),
    path('porcentagem/', views.porcentagem, name='porcentagem'),
    path('getVistoriaMaisRescente/', views.getVistoriaMaisRescente, name='getVistoriaMaisRescente'),


]
from django.urls import path
from pesquisas import views

urlpatterns = [
    path('cadastrarPesquisa/', views.cadastrarPesquisa, name='cadastrarPesquisa'),
    path('consultarPesquisa/', views.consultarPesquisa, name='consultarPesquisa'),
    path('filtrarPais/', views.filtrar_Pais, name='filtrarPais'),
]
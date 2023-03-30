from django.contrib import admin
from django.urls import path
from app.views import EnderecoViewSets, CadastroViewSets

urlpatterns = [
    path(r'Cadastro/', EnderecoViewSets),
    path(r'Endereco/', CadastroViewSets),
]

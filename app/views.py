from django.shortcuts import render
from rest_framework import viewsets
from app.models import Endereco, Cadastro
from app.serializers import EnderecoSeializer,CadastroSeializer
# Create your views here.

class EnderecoViewSets(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSeializer


class CadastroViewSets(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSeializer
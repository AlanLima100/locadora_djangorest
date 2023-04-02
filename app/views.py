from django_filters import rest_framework as filters
from rest_framework import viewsets 
from app.serializers import EnderecoSerializer,CadastroSerializer, FilmeSerializer, LocacaoSerializer, AvaliacaoSerializer, DevolucaoSerializer

from app.models import Endereco, Cadastro, Filme, Locacao, Avaliacao, Devolucao

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class LocacaoViewSet(viewsets.ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer
    filterset_fields = {
        'data_hora_locacao': ['exact', 'gte', 'lte'],
    }
    filter_backends = [filters.DjangoFilterBackend]


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class DevolucaoViewSet(viewsets.ModelViewSet):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer
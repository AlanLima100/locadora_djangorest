from rest_framework import serializers #importando o serializers que é como se fosse o template
from app.models import Endereco, Cadastro, Filme, Locacao, Avaliacao, Devolucao


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','rua', 'numero_rua', 'bairro', 'cidade', 'cep']


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['id','nome', 'sobrenome', 'data_nascimento', 'telefone', 'email', 'cpf', 'endereco']


class FilmeSerializer(serializers.ModelSerializer):
    queryset = Filme.objects.all()
    class Meta:
        model = Filme
        fields = ['id','nome', 'ano', 'genero', 'sinopse', 'sensura', 'avaliacoes']


class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locacao
        fields = ['id','usuario', 'locou', 'data_hora_locacao']

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id','nota', 'comentario']


class DevolucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucao
        fields = ['id','filme_devolucao', 'devolucao_avaliacao']
from rest_framework import serializers #importando o serializers que é como se fosse o template
from app.models import Endereco, Cadastro, Filme, Locacao, Avaliacao, Devolucao


class EnderecoSeializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero_rua', 'bairro', 'cidade', 'cep']


class CadastroSeializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['nome', 'sobrenome', 'data_nascimento', 'telefone', 'email', 'cpf', 'endereco']


# class EnderecoSeializer(serializers.ModelSerializer):
#     class Meta:
#         model = Filme


# class EnderecoSeializer(serializers.ModelSerializer):
#     class Meta:
#         model = Locacao

# class EnderecoSeializer(serializers.ModelSerializer):
#     class Meta:
#         model = Avaliacao, Devolucao


# class EnderecoSeializer(serializers.ModelSerializer):
#     class Meta:
#         model = Devolucao
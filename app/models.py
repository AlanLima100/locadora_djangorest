from django.db import models
from datetime import datetime
from django.core.validators import MaxLengthValidator

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField(max_length=120)
    numero_rua = models.CharField(max_length=15)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    cep = models.CharField(max_length=9)


class Cadastro(models.Model):
    nome = models.CharField(max_length=150, validators=[MaxLengthValidator(150)])
    sobrenome = models.CharField(max_length=150)
    data_nascimento =  models.DateField()
    telefone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    cpf = models.CharField(max_length=14, validators=[MaxLengthValidator(14)])
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


class Filme(models.Model):
  
    nome = models.CharField(max_length=150) 
    ano = models.IntegerField()
    genero = models.CharField(max_length=15)
    sinopse = models.CharField(max_length=300)
    sensura = models.CharField(max_length=25)
    avaliacoes = models.ManyToManyField('Avaliacao', blank=True)


class Locacao(models.Model):
    

    usuario = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    locou = models.ManyToManyField(Filme, blank=True)
    data_hora_locacao = models.DateTimeField(default=datetime.now, editable=False, verbose_name="Data e hora da locação")


class Avaliacao(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField()
    

class Devolucao(models.Model):
    filme_devolucao = models.ManyToManyField('Filme', blank=True)
    devolucao_avaliacao = models.ManyToManyField('Avaliacao', blank=True)

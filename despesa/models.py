from django.db import models

class Despesa(models.Model):
    TIPO_CHOICES = [
        (1,'Remedio'),
        (2, 'Roupas'),
        (3, 'Alimentacao'),
        (4, 'Educacao'),
        (5, 'Transporte'),
        (6, 'Outos'),
    ]
    FORMA_PAGAMENTO_CHOICES =[
        (1,'Dinheiro'),
        (2,'Cartão de Crédito'),
        (3, 'Cartão de Débito'),
        (4, 'Cartão Crediário'),
        (5, 'Cheque'),
    ]
    data_criacao = models.DateTimeField()
    tipo = models.IntegerField(
        max_length= 100,
        choices=TIPO_CHOICES,
        default=1,
        )
    descricao = models.CharField(max_length=500)
    forma_pagamento = models.CharField(
        max_length=255,
        choices=FORMA_PAGAMENTO_CHOICES,
        default=1
    )
    vencimento = models.DateTimeField()
    quitado = models.BooleanField()

    def __str__(self):
        return self.data_criacao


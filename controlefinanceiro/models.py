from django.db import models

# Create your models here.
class ClassificacaoPagar(models.Model):
    descricao = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )    

    PAGAR = 'pagar'
    RECEBER = 'receber'

    tipo_choices = [        
        (PAGAR, 'pagar'),
        (RECEBER, 'receber')
    ]

    tipo = models.CharField(
        max_length=10,
        choices=tipo_choices,
        default=PAGAR,
    )

    objetos = models.Manager()

class FormaPagamento(models.Model):
    descricao = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )    

    objetos = models.Manager()    


class ContasPagar(models.Model):
    PAGO = 'Pago'
    PAGAR = 'A pagar'

    situacao_pagar_choices = [
        (PAGO, 'Pago'),
        (PAGAR, 'A pagar'),
    ]

    data_vencimento = models.DateField(
        null=False,
        default='2020-01-01'
    )
    
    data_pagamento = models.DateField(
        null=False,
        default='2020-01-01'
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    situacao = models.CharField(
        max_length=10,
        choices=situacao_pagar_choices,
        default=PAGAR,
    )

    classificacoes = models.ForeignKey(
        ClassificacaoPagar, on_delete=models.CASCADE,
        default=3
    )
    
    formaspagamento = models.ForeignKey(
        FormaPagamento, on_delete=models.CASCADE,
        default=1
    )

    objetos = models.Manager()

class ContasReceber(models.Model):
    RECEBIDO = 'Recebido'
    RECEBER = 'A receber'   

    situacao_receber_choices = [
        (RECEBIDO, 'Recebido'),
        (RECEBER, 'A receber'),
    ]

    data_expectativa = models.DateTimeField()
    data_recebimento = models.DateTimeField()
    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    situacao = models.CharField(
        max_length=10,
        choices=situacao_receber_choices,
        default=RECEBIDO,
    )

    classificacoes = models.ForeignKey(
        ClassificacaoPagar, on_delete=models.CASCADE,
        default=7
    )
    
    formaspagamento = models.ForeignKey(
        FormaPagamento, on_delete=models.CASCADE,
        default=1
    )

    objetos = models.Manager()







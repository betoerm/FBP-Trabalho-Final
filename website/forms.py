from django import forms
from controlefinanceiro.models import ContasPagar, ContasReceber, ClassificacaoPagar, FormaPagamento

class InsereContasPagarForm(forms.ModelForm):                        
    class Meta:
        model = ContasPagar
        fields = [
            'data_vencimento',
            'data_pagamento',
            'valor',
            'descricao',
            'situacao'
        ]

    classificacoes = forms.ModelMultipleChoiceField(queryset=ClassificacaoPagar.objetos.all())

    formaspagamento = forms.ModelMultipleChoiceField(queryset=FormaPagamento.objetos.all())

class InsereContasReceberForm(forms.ModelForm):                        
    class Meta:
        model = ContasReceber
        fields = [
            'data_expectativa',
            'data_recebimento',
            'valor',
            'descricao',
            'situacao'
        ]

    classificacoes = forms.ModelMultipleChoiceField(queryset=ClassificacaoPagar.objetos.all())    

    formaspagamento = forms.ModelMultipleChoiceField(queryset=FormaPagamento.objetos.all())

class InsereClassificaoPagarForm(forms.ModelForm):
    class Meta:
        model = ClassificacaoPagar
        fields = [
            'descricao'
        ]

class InsereFormasPagamento(forms.ModelForm):
    class Meta:
        model = FormaPagamento
        fields = [
            'descricao'
        ]        
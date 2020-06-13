from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from controlefinanceiro.models import ContasPagar, ContasReceber, ClassificacaoPagar, FormaPagamento

class InsereContasPagarForm(forms.ModelForm):         

    class Meta:
        model = ContasPagar

        fields = [           
            'data_vencimento',
            'data_pagamento',
            'valor',
            'descricao',
            'situacao',            
            'classificacoes',
            'formaspagamento'
        ]

        labels = {
            'data_vencimento': 'Data de Vencimento',
            'data_pagamento': 'Data de Pagamento ',
            'valor': 'Valor',
            'descricao': 'Descrição',
            'situacao': 'Situação',
            'classificacoes': 'Classificação',
            'formaspagamento': 'Forma de Pagamento'
        }

        widgets = {            
            'data_vencimento': DateTimePickerInput(format='%Y-%m-%d'), # specify date-frmat
            'data_pagamento': DateTimePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }

class InsereContasReceberForm(forms.ModelForm):                        
    class Meta:
        model = ContasReceber
        fields = [
            'data_expectativa',
            'data_recebimento',
            'valor',
            'descricao',
            'situacao',
            'classificacoes',
            'formaspagamento' 
        ]
        labels = {
            'data_expectativa': 'Data de Expectativa de Recebimento',
            'data_recebimento': 'Data de Recebimento ',
            'valor': 'Valor',
            'descricao': 'Descrição',
            'situacao': 'Situação',
            'classificacoes': 'Classificação',
            'formaspagamento': 'Forma de Pagamento'
        }

        widgets = {            
            'data_expectativa': DateTimePickerInput(format='%Y-%m-%d'), # specify date-frmat
            'data_recebimento': DateTimePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }

class InsereClassificaoPagarForm(forms.ModelForm):
    class Meta:
        model = ClassificacaoPagar
        fields = [
            'descricao',
            'tipo'
        ]

class InsereFormasPagamento(forms.ModelForm):
    class Meta:
        model = FormaPagamento
        fields = [
            'descricao'
        ]        
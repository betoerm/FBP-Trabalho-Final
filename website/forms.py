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
            'situacao'
        ]

        widgets = {            
            'data_vencimento': DateTimePickerInput(format='%Y-%m-%d'), # specify date-frmat
            'data_pagamento': DateTimePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }

    classificacoes = forms.ChoiceField(
            choices=[(cl.pk, cl.descricao) for cl in ClassificacaoPagar.objetos.all().filter(tipo='pagar')],
        ) 

    formaspagamento =  forms.ChoiceField(
        choices=[(cl.pk, cl.descricao) for cl in FormaPagamento.objetos.all()]
    ) 

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

        widgets = {            
            'data_expectativa': DateTimePickerInput(format='%Y-%m-%d'), # specify date-frmat
            'data_recebimento': DateTimePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }

    classificacoes =  forms.ChoiceField(
            choices=[(cl.pk, cl.descricao) for cl in ClassificacaoPagar.objetos.all().filter(tipo='receber')],
        ) 

    formaspagamento =  forms.ChoiceField(
        choices=[(cl.pk, cl.descricao) for cl in FormaPagamento.objetos.all()]
    ) 

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
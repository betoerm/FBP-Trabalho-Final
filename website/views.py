from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.db.models.functions import Cast
from django.db.models import Sum
from controlefinanceiro.models import ContasPagar, ContasReceber, ClassificacaoPagar, FormaPagamento
from website.forms import InsereContasPagarForm, InsereContasReceberForm, InsereClassificaoPagarForm, InsereFormasPagamento

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

#CONTAS A PAGAR ---------------------------------------------------------------    

class ContasPagarCreateView(CreateView):
    template_name = "website/contaspagar/criacontaspagar.html"
    model = ContasPagar
    form_class = InsereContasPagarForm
    success_url = reverse_lazy("website:lista_contas_pagar")

class ContasPagarListView(ListView):
    template_name = "website/contaspagar/listacontaspagar.html"
    model = ContasPagar    
    context_object_name = "contaspagar"

class ContasPagarUpdateView(UpdateView):
    template_name = "website/contaspagar/atualizacontaspagar.html"    
    model = ContasPagar
    fields = '__all__'
    context_objetc_name = "contaspagar"
    success_url = reverse_lazy("website:lista_contas_pagar")

class ContasPagarDeleteView(DeleteView):
    template_name = "website/contaspagar/excluicontaspagar.html"
    model = ContasPagar
    context_objetc_name = "contaspagar"
    success_url = reverse_lazy("website:lista_contas_pagar")

#CONTAS A RECEBER ---------------------------------------------------------------    

class ContasReceberCreateView(CreateView):
    template_name = "website/contasreceber/criacontasreceber.html"
    model = ContasReceber
    form_class = InsereContasReceberForm
    success_url = reverse_lazy("website:lista_contas_receber")

class ContasReceberListView(ListView):
    template_name = "website/contasreceber/listacontasreceber.html"
    model = ContasReceber
    context_object_name = "contasreceber"

class ContasReceberUpdateView(UpdateView):
    template_name = "website/contasreceber/atualizacontasreceber.html"    
    model = ContasReceber
    fields = '__all__'
    context_objetc_name = "contasreceber"
    success_url = reverse_lazy("website:lista_contas_receber")

class ContasReceberDeleteView(DeleteView):
    template_name = "website/contasreceber/excluicontasreceber.html"
    model = ContasReceber
    context_objetc_name = "contasreceber"
    success_url = reverse_lazy("website:lista_contas_receber")


#CLASSIFICAÇÃO DE CONTAS ---------------------------------------------------------------    

class ClassificacaoPagarCreateView(CreateView):
    template_name = "website/classificacaopagar/criaclassificacaopagar.html"
    model = ClassificacaoPagar
    form_class = InsereClassificaoPagarForm
    success_url = reverse_lazy("website:lista_classificacao_pagar")


class ClassificacaoPagarListView(ListView):
    template_name = "website/classificacaopagar/listaclassificacaopagar.html"
    model = ClassificacaoPagar
    context_object_name = "classificacaopagar"  

class ClassificacaoPagarUpdateView(UpdateView):
    template_name = "website/classificacaopagar/atualizaclassificacaopagar.html"    
    model = ClassificacaoPagar
    fields = '__all__'
    context_objetc_name = "classificacaopagar"
    success_url = reverse_lazy("website:lista_classificacao_pagar")

class ClassificacaoPagarDeleteView(DeleteView):
    template_name = "website/classificacaopagar/excluiclassificacaopagar.html"
    model = ClassificacaoPagar
    context_objetc_name = "classificacaopagar"
    success_url = reverse_lazy("website:lista_classificacao_pagar")   


#FORMAS DE PAGAMENTOS ---------------------------------------------------------------    
class FormasPagamentoListView(ListView):
    template_name = "website/formapagamento/listaformaspagamento.html"
    model = FormaPagamento
    context_object_name = "formapagamento"  

class FormasPagamentoCreateView(CreateView):
    template_name = "website/formapagamento/criaformaspagamento.html"
    model = FormaPagamento
    form_class = InsereFormasPagamento
    success_url = reverse_lazy("website:lista_formas_pagamento")

class FormasPagamentoUpdateView(UpdateView):
    template_name = "website/formapagamento/atualizaformaspagamento.html"    
    model = FormaPagamento
    fields = '__all__'
    context_objetc_name = "formapagamento"
    success_url = reverse_lazy("website:lista_formas_pagamento")

class FormasPagamentoDeleteView(DeleteView):
    template_name = "website/formapagamento/excluiformaspagamento.html"
    model = FormaPagamento
    context_objetc_name = "formapagamento"
    success_url = reverse_lazy("website:lista_formas_pagamento")   


class FluxoListView(ListView):
    template_name= "website/fluxo.html"

    context_object_name = "fluxo"       

    def get_queryset(self):
        return ContasPagar.objetos.order_by("data_vencimento").values('descricao', 'data_vencimento', 'data_pagamento', 'valor',
         'situacao')

    def get_context_data(self, **kwargs):
        context = super(FluxoListView, self).get_context_data(**kwargs  )
        context ['fluxoreceber']= {
            'fluxoreceber': ContasReceber.objetos.order_by("data_expectativa").values('descricao', 'data_expectativa',
                'data_recebimento', 'valor', 'situacao'), 
            'total_pagar': ContasPagar.objetos.all().filter(situacao = 'A pagar').aggregate(Sum('valor')),
            'total_receber': ContasReceber.objetos.all().filter(situacao = 'Recebido').aggregate(Sum('valor'))
        }
        return context

    
    
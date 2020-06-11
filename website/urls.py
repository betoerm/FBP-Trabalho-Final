from django.urls import path
from website.views import IndexTemplateView, ContasPagarListView, ContasPagarUpdateView, ContasPagarDeleteView, ContasPagarCreateView
from website.views import ClassificacaoPagarCreateView, ClassificacaoPagarListView, ClassificacaoPagarUpdateView, ClassificacaoPagarDeleteView
from website.views import ContasReceberCreateView, ContasReceberDeleteView, ContasReceberListView, ContasReceberUpdateView
from website.views import FormasPagamentoListView, FormasPagamentoCreateView, FormasPagamentoUpdateView, FormasPagamentoDeleteView
from website.views import FluxoListView

app_name = 'website'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    #Contas a pagar
    path('contaspagar/cadastrar/', ContasPagarCreateView.as_view(), name = "cria_contas_pagar"),
    path('contaspagar/', ContasPagarListView.as_view(), name="lista_contas_pagar"),
    path('contaspagar/<pk>', ContasPagarUpdateView.as_view(), name="atualiza_contas_pagar"),
    path('contaspagar/excluir/<pk>', ContasPagarDeleteView.as_view(), name="exclui_contas_pagar"),

    #Contas a receber
    path('contasreceber/cadastrar/', ContasReceberCreateView.as_view(), name = "cria_contas_receber"),
    path('contasreceber/', ContasReceberListView.as_view(), name="lista_contas_receber"),
    path('contasreceber/<pk>', ContasReceberUpdateView.as_view(), name="atualiza_contas_receber"),
    path('contasreceber/excluir/<pk>', ContasReceberDeleteView.as_view(), name="exclui_contas_receber"),
        
    #Classificação de contas a pagar
    path('classificacaopagar/cadastrar/', ClassificacaoPagarCreateView.as_view(), name = "cria_classificacao_pagar"),
    path('classificacaopagar/', ClassificacaoPagarListView.as_view(), name="lista_classificacao_pagar"),
    path('classificacaopagar/<pk>', ClassificacaoPagarUpdateView.as_view(), name="atualiza_classificacao_pagar"),
    path('classificacaopagar/excluir/<pk>', ClassificacaoPagarDeleteView.as_view(), name="exclui_classificacao_pagar"),

    #Formas de pagamento
    path('formaspagamento/cadastrar/', FormasPagamentoCreateView.as_view(), name = "cria_formas_pagamento"),
    path('formaspagamento/', FormasPagamentoListView.as_view(), name="lista_formas_pagamento"),
    path('formaspagamento/<pk>', FormasPagamentoUpdateView.as_view(), name="atualiza_formas_pagamento"),
    path('formaspagamento/excluir/<pk>', FormasPagamentoDeleteView.as_view(), name="exclui_formas_pagamento"),

    #FLUXOS
    path('fluxo/', FluxoListView.as_view(), name = "fluxo"),   
    path('fluxomensal/', FluxoListView.as_view(), name = "fluxomensal")
]
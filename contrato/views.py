# Create your views here.
from django.shortcuts import render
from contrato.models import Contrato
from contrato.forms import ContratoForms
from pagamento.models import Pagamento
from pagamento.forms import PagamentoForms
from django.shortcuts import redirect


def abrir_contratos(request):
    contratos = Contrato.objects.all()
    dados = {
        'dados' : contratos
    }
    return render(request, "contrato/contrato.html", dados)

def abrir_novo_contrato(request):
    if request.method == "GET":
        form_contrato =  ContratoForms()
        dados = {
            'form' : form_contrato,
            'save' : False,    
        }
        return render(request, 'contrato/novo.html', dados)
    else:
        form = ContratoForms(request.POST)
        
        if form.is_valid():
           contrato = form.save()
           form = ContratoForms()
           dados = {
                'form' : form,
                'save' : True,   
            }
        else:
            dados = {
                'form' : form,
                'save' : False,   
            }
        
        return render(request, 'contrato/novo.html', dados)
            
def abrir_detalhes_do_contrato(request, id):
    
    contrato = Contrato.objects.get(id=id)
    pagamentos = Pagamento.objects.filter(id_contrato=id)

    for pagamento in pagamentos:
        pagamento.form_pagamento = PagamentoForms(instance=Pagamento.objects.get(id=pagamento.id))    
    

    dados = {
        'id': str(id),
        'contrato': ContratoForms(instance=contrato),
        'form_pagamento': PagamentoForms(),
        'pagamentos' : pagamentos,
        'save': False,
    }
    
    if request.method == "POST":

        def validar_novo_pagamento():
            request_novo_pagamento = request.POST
            novo_pagamento = Pagamento()
            novo_pagamento.id_contrato = Contrato.objects.get(id=id)
            novo_pagamento.valor = request_novo_pagamento['valor']
            novo_pagamento.data_de_vencimento = request_novo_pagamento['data_de_vencimento'] 
            novo_pagamento.numero_do_processo = request_novo_pagamento['numero_do_processo']
            novo_pagamento.status = request_novo_pagamento['status']
            if PagamentoForms(request.POST, instance=novo_pagamento).is_valid():
                novo_pagamento.save()
            
                dados.update({
                    'pagamentos': Pagamento.objects.filter(id_contrato=id),
                    'contrato': ContratoForms(instance=contrato),
                    'save': True,
                    'msg': 'Pagamento incluído'
                })
            else:
                dados.update({
                    'form_pagamento': PagamentoForms(request.POST)
                })
            return dados

        def atulizar_contrato():
            contrato_update = ContratoForms(request.POST, instance=contrato)
            if contrato_update.is_valid():
                contrato_update.save()
            dados.update({
                'contrato': contrato_update,
                'save': True,
                'msg': 'Contrato atualizado'
            })
            return dados

        def apagar_pagamento():
            id_pagamento = int(request.POST["apagar_pagamento"])
            pagamento = Pagamento.objects.get(id=id_pagamento)
            pagamento.delete()
            dados.update({
                'pagamentos': Pagamento.objects.filter(id_contrato=id),
                'save': True,
                'msg': 'Pagamento excluido'
            })
            return dados

        def atulizar_pagamento():
            pagamento_atulizado = PagamentoForms(request.POST, instance=pagamento )
            if pagamento_atulizado.is_valid():
                pagamento.save()

                dados.update({
                    'pagamentos': Pagamento.objects.filter(id_contrato=id),
                    'save': True,
                    'msg': 'Pagamento atulizado'
                })
                return dados
           
            else:
                dados.update({
                    'form_pagamento': PagamentoForms(request.POST)
                })
                return dados

        acao = list(dict(request.POST).keys())[1]
        
        dict_de_acoes = {
            'novo_pagamento' : lambda: validar_novo_pagamento(),
            'apagar_pagamento' : lambda: apagar_pagamento(),
            'atulizar_pagamento' : lambda: atulizar_pagamento(),
            'atulizar_contrato' : lambda: atulizar_contrato(),
        }
        
        fcn = dict_de_acoes[acao]
        dados = fcn()

        return render(request, 'contrato/detalhes.html', dados)

    return render(request, 'contrato/detalhes.html', dados)

# Create your views here.
from django.shortcuts import render
from contrato.models import Contrato
from contrato.forms import ContratoForms
from pagamento.models import Pagamento
from pagamento.forms import PagamentoForms


# Create your views here.
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
    if request.method == "GET":
        dados = {
            'id': str(id),
            'contrato': ContratoForms(instance=contrato),
            'form_pagamento': PagamentoForms(),
            'pagamentos' : pagamentos,
            'save': False,
        }
    elif request.method == "POST":

        if 'contrato'  in request.POST:
            contrato_update = ContratoForms(request.POST, instance=contrato)
            if contrato_update.is_valid():
                contrato_update.save()
            dados = {
                'id': str(id),
                'contrato': contrato_update,
                'form_pagamento': PagamentoForms(),
                'pagamentos' : pagamentos,
                'save': True,
                'msg': 'Contrato atualizado'
            }
        
        elif 'apagar_pagamento' in request.POST:
            id_pagamento = int(request.POST["apagar_pagamento"])
            pagamento = Pagamento.objects.get(id=id_pagamento)
            pagamento.delete()
            dados = {
                'id': str(id),
                'contrato': ContratoForms(instance=contrato),
                'form_pagamento': PagamentoForms(),
                'pagamentos' : pagamentos,
                'save': True,
                'msg': 'Pagamento excluido'

            } 

        elif 'novo_pagamento' in request.POST:
            request_novo_pagamento = request.POST
            novo_pagamento = Pagamento()
            novo_pagamento.id_contrato = Contrato.objects.get(id=id)
            novo_pagamento.valor = request_novo_pagamento['valor']
            novo_pagamento.data_de_vencimento = request_novo_pagamento['data_de_vencimento'] 
            novo_pagamento.numero_do_processo = request_novo_pagamento['numero_do_processo']
            novo_pagamento.status = request_novo_pagamento['status']
            if PagamentoForms(request.POST, instance=novo_pagamento).is_valid():
                novo_pagamento.save()
            
                dados = {
                    'id': str(id),
                    'contrato': ContratoForms(instance=contrato),
                    'form_pagamento': PagamentoForms(),
                    'pagamentos' : pagamentos,
                    'save': True,
                    'msg': 'Pagamento incluído'
                }
            else:
                dados = {
                    'id': str(id),
                    'contrato': ContratoForms(instance=contrato),
                    'pagamentos' : pagamentos,
                    'form_pagamento': PagamentoForms(request.POST)
                    
                }

        else:
            request_pagamento = request.POST
            pagamento = Pagamento.objects.get(id=request_pagamento['id'])
            pagamento.valor = float(request_pagamento['valor'].replace(',','.'))
            pagamento.data_de_vencimento = request_pagamento['data_de_vencimento']
            pagamento.status = request_pagamento['status']
            pagamento.numero_do_processo = request_pagamento['numero_do_processo']
            pagamento.save()

            dados = {
                'id': str(id),
                'contrato': ContratoForms(instance=contrato),
                'form_pagamento': PagamentoForms(),
                'pagamentos' : pagamentos,
                'save': True,
                'msg': 'Pagamento atulizado'
            }

    return render(request, 'contrato/detalhes.html', dados)
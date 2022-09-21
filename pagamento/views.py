from django.http import HttpResponse
from django.shortcuts import render
from pagamento.forms import PagamentoForms
from pagamento.models import Pagamento

# Create your views here.

def abrir_novo_pagamento(request, id):
    dados = {
        'id_contrato' : id,
        'form_pagamento' : PagamentoForms()
    }

    return render(request, 'pagamento/novo.html', dados)

def editar_pagamento(request, id_pagamento):
    pagamento_editar = Pagamento.objects.get(id=id_pagamento)
    form_pagemento_editar = PagamentoForms(instance=pagamento_editar)
    return HttpResponse(form_pagemento_editar)
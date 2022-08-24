# Create your views here.
from django.shortcuts import render
from contrato.models import Contrato
from contrato.forms import ContratoForms


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
            
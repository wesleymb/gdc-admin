from django import forms
from pagamento.models import Pagamento
from GDC import settings

class PagamentoForms(forms.ModelForm):
    class Meta:
        model = Pagamento
        
        fields = ( 
            'valor',
            'data_de_vencimento',
            'numero_do_processo',
            'status',
        )

        widgets = {
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'data_de_vencimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format=settings.DATE_INPUT_FORMATS),
            'numero_do_processo': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
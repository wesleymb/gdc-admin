from django import forms
from contrato.models import Contrato
from GDC import settings

class ContratoForms(forms.ModelForm):
    class Meta:
        model = Contrato
        
        fields = "__all__"
        
        widgets = {
            'contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_de_processo': forms.TextInput(attrs={'class': 'form-control'}),
            'objeto': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'data_assinatura': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format=settings.DATE_INPUT_FORMATS),
            'data_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format=settings.DATE_INPUT_FORMATS),
            'vencimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format=settings.DATE_INPUT_FORMATS),
            'servidor_gestor': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "contato_da_empresa" : forms.TextInput(attrs={'class': 'form-control'}),
            "email_da_empresa" : forms.TextInput(attrs={'class': 'form-control'}),
            "telefone" : forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }


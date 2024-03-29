from contrato import views
from django.urls import path

urlpatterns = [
    path('', views.abrir_contratos, name='contratos'),
    path('novo_contrato/', views.abrir_novo_contrato, name='novo_contrato'),
    path('detalhes_contrato/<int:id>', views.abrir_detalhes_do_contrato, name='detalhes_contrato/'),
]
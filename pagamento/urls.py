from pagamento import views
from django.urls import path

urlpatterns = [
    path('novo_pagamento/', views.abrir_novo_pagamento, name='novo_pagamento'),
    path('editar_pagamento/<int:id_pagamento>', views.editar_pagamento, name='editar_pagamento/'),
]
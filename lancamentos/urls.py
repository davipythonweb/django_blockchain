from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_blocos, name='lista_blocos'),
    path('novo/', views.adiciona_lancamento, name='adiciona_lancamento'),
]

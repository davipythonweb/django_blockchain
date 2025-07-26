from django.shortcuts import render, redirect
from .models import Bloco
import json
import time

def adiciona_lancamento(request):
    if request.method == "POST":
        conta = request.POST.get("conta")
        debito = float(request.POST.get("debito", 0))
        credito = float(request.POST.get("credito", 0))

        dados = json.dumps({
            "conta": conta,
            "debito": debito,
            "credito": credito,
            "timestamp": time.time()
        })

        ultimo = Bloco.objects.order_by('-index').first()
        index = 0 if not ultimo else ultimo.index + 1
        hash_anterior = "0" if not ultimo else ultimo.hash

        novo = Bloco(index=index, dados=dados, hash_anterior=hash_anterior)
        novo.minera_bloco(dificuldade=3)
        novo.save()

        return redirect('lista_blocos')

    return render(request, 'lancamentos/adiciona_lancamento.html')


def lista_blocos(request):
    blocos = Bloco.objects.all().order_by('index')
    return render(request, 'lancamentos/lista_blocos.html', {'blocos': blocos})

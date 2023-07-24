from django.shortcuts import render, redirect
from .forms import Sorveteforms
from .models import Sorvete


def sorvete_pedido(request):
    if request.method=='POST':
        print('to aqui')
        form = Sorveteforms(request.POST)
        form.save()
        return redirect('pedido')# redireciona para a pagina de sucesso após salvar
    else:
        form = Sorveteforms()
    return render(request, 'main/index.html', {'form':form})


def pedidos(request):
    query = Sorvete.objects.all()

    return render(request, 'main/lista.html', {'query':query})


def produtos(request):
    return render(request,'main/produtos.html')
from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.filter(destaque=True)
    return render(request, 'loja/index.html', {'produtos': produtos})
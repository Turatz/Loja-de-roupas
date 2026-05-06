from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Produto

def index(request):
    produtos = Produto.objects.filter(destaque=True)
    return render(request, 'loja/index.html', {'produtos': produtos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            return redirect('index')
        else:
            return render(request, 'loja/login.html', {'erro': 'Usuário ou senha incorretos'})
    return render(request, 'loja/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'loja/cadastro.html', {'erro': 'Usuário já existe'})
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'loja/cadastro.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def categoria_view(request, categoria):
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'loja/categoria.html', {'produtos': produtos, 'categoria': categoria})
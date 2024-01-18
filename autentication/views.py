from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth

def cadastro(request):
        try:
            if request.method == "GET":
                return render(request, 'index.html') 
            elif request.method == "POST":
                nomeUsuario = request.POST.get("username")
                senhaUsuario = request.POST.get("senha")
                confirmarSenhaUsuario = request.POST.get("confirmar_senha")

            usuarios = User.objects.filter(username=nomeUsuario)

            if not senhaUsuario == confirmarSenhaUsuario:
                messages.add_message(request, constants.ERROR, 'Senhas não coicidem')
                return redirect("/autentication/login")
            elif usuarios == [nomeUsuario]:
                print(usuarios)
                messages.add_message(request, constants.ERROR, 'Nome de usuário já está em uso')
                return redirect("/autentication/login")
            else:
                User.objects.create_user(
                    username = nomeUsuario,
                    password = senhaUsuario,
                )
            return redirect("/autentication/logar")
        except: 
            messages.add_message(request, constants.ERROR, 'Nome de usuário já está em uso')
            return redirect("/autentication/login")
        
def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(request, username=usuario, password=senha)
        if user == None:
            messages.add_message(request, constants.ERROR, 'Não deu para logar')
            return redirect("/autentication/logar")
        else:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'usuário logado!!')
            return redirect("/autentication/logar")

def logout(request):
    auth.logout(request)
    return redirect('autentication/logar')   
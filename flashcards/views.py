from django.shortcuts import render, redirect
from .models import Categoria, Flashcard
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.

def flash(request):
    if not request.user.is_authenticated:
        return redirect('/autentication/logar')
    if request.method == "GET":
        categoria = Categoria.objects.all()
        dificuldade = Flashcard.DIFICULDADE_CHOICES
        
        categoriaFiltro = request.GET.get('categoriaFiltro')
        dificuldadeFiltro = request.GET.get('dificuldadeFiltro')
        
        if (categoriaFiltro == None or dificuldadeFiltro == None):
            flashs = Flashcard.objects.filter(user_id=request.user.id)
        else:
            flashs = Flashcard.objects.filter(user_id=request.user.id, categoria_id=categoriaFiltro, dificuldade=dificuldadeFiltro)
           
        return render(request, 'flashcards.html', {'categoria': categoria, 'dificuldade': dificuldade, 'flashs': flashs})
    if request.method == "POST":
        pergunta = request.POST.get("pergunta")
        resposta = request.POST.get("resposta")
        categoria = request.POST.get("categoria")
        dificuldade = request.POST.get("dificuldade")
        
        if len(pergunta.strip()) == 0 or len(resposta.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Por favor, preencha os campos')
            return redirect('/flashcards')
        
        Flashcard.objects.create(
            pergunta = pergunta,
            resposta = resposta,
            dificuldade = dificuldade,
            categoria_id = categoria,
            user = request.user
        )
        messages.add_message(request, constants.SUCCESS, 'FlashCard cadastrado com sucesso')
        return redirect('/flashcards')
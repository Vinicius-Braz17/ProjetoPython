from django.urls import path
from . import views

urlpatterns = [
    path('', views.flash, name='flashcards'),
    path('deletarFlashCards/<int:id>', views.deletar_flashCards, name='deletar_flashCards'),
    path('iniciarDesafio', views.iniciar_desafio, name='iniciar_desafio'),
]

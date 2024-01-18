from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.cadastro, name='login'),
    path('logar/', views.logar, name='logado'),
    path('logout', views.logout, name='logout')
]
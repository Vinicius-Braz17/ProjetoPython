from django.urls import path
from . import views

urlpatterns = [
    path('', views.flash, name='/princ')
]

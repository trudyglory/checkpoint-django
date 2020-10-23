# pages/urls.py
from django.urls import path
from .views import accueilView

urlpatterns = [
    path('', accueilView, name='accueil')
]
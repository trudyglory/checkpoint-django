# pages/views.py 
from django.http import HttpResponse

def accueilView(request):
    return HttpResponse("Bienvenue à l'accueil des cartes de voyage")


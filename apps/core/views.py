from django.shortcuts import render
from django.urls import reverse

def home_view(request):
    breadcumbs  = [
        ("Page d'accueil", reverse('index'))
        ]
    
    return render(request, 'core/index.html', {'breadcumbs' : breadcumbs}  )
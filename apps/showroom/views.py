from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def components_view(request):
    breadcumbs  = [
        ("Page d'accueil", reverse_lazy('index')),
        ("Composants", reverse_lazy('components')),
        ]
    
    return render(request, 'showroom/components.html', {'breadcumbs' : breadcumbs}  )

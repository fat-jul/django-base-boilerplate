from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def home_view(request):
    breadcumbs  = [
        ("Page d'accueil", reverse_lazy('index'))
        ]
    
    return render(request, 'core/index.html', {'breadcumbs' : breadcumbs}  )

@login_required
def test_view(request):
    breadcumbs  = [
        ("Page de test login", reverse_lazy('test'))
        ]
    
    return render(request, 'core/indexcopy.html', {'breadcumbs' : breadcumbs}  )

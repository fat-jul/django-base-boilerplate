from django.urls import path
from .views import home_view, test_view

urlpatterns = [
    path('', home_view, name='index'),
    path('test/', test_view, name='test'),
    
    
    
]
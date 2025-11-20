from django.urls import path
from .views import components_view

urlpatterns = [
    path('', components_view, name='components'),
    
]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings #Bonne pratique, meilleur que 'from .settings import DEBUG'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
]


# Ajout de la gestion des fichiers média pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
from django.urls import path, include
from .views import AppointmentViewSet
from rest_framework.routers import DefaultRouter

# Criando o roteador para registrar os endpoints da API
router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)  # Registrar o viewset

# Definir o padrão de URL para o seu aplicativo
urlpatterns = [
    # Inclui as URLs da API usando o roteador
    path('api/', include(router.urls)),
]

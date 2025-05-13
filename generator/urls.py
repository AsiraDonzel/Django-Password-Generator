from django.urls import path
from .views import home, generate_password

urlpatterns = [
    path('', home, name='home'),
    path('generate/', generate_password, name='generate_password'),
]

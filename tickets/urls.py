from django.urls import path

from .views import home, create

urlpatterns = [
    path('', home, name='home'),
    path('tickets/create/', create, name='create_ticket'),
]
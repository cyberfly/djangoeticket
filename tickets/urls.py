from django.urls import path

from .views import home, create, index

urlpatterns = [
    path('', home, name='home'),
    path('tickets/create/', create, name='create_ticket'),
    path('tickets/', index, name='index_ticket'),
]
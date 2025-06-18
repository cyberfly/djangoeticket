from django.urls import path

from .views import home, create, index, show

urlpatterns = [
    path('', home, name='home'),
    path('tickets/create/', create, name='create_ticket'),
    path('tickets/', index, name='index_ticket'),
    path('tickets/<int:ticket_id>/', show, name='show_ticket'),
]
from django.urls import path

from .views import home, create, index, show
from .views_admin import index as admin_index

urlpatterns = [
    path('', home, name='home'),
    path('tickets/create/', create, name='create_ticket'),
    path('tickets/', index, name='index_ticket'),
    path('tickets/<int:ticket_id>/', show, name='show_ticket'),
    path('pentadbir/tickets/', admin_index, name='admin_index_ticket'),
]
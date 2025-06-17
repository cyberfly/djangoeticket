from django.shortcuts import render
from .models import Ticket

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):

    if request.method == 'POST':
        # bila submit form

        #  print untuk lihat data yang dihantar
        print("Form data", request.POST)

        # get data from post request
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')

        user = request.user

        # try create a new ticket
        Ticket.objects.create(title=title, description=description, user=user)
        
        
    else:
        # bila papar form
        pass

    return render(request, 'tickets/create.html')
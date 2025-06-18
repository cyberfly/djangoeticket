from django.shortcuts import render
from .models import Ticket
from lookups.models import Department, Category
from .forms import CreateTicketForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, "home.html")

def index(request):

    tickets = Ticket.objects.filter(user=request.user).order_by("-created_at")

    # initialize paginator
    page_size = 5
    paginator = Paginator(tickets, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # breakpoint()
    # end initialize paginator

    # breakpoint()
    context = {
        "page_obj": page_obj,
    }

    return render(request, "tickets/index.html", context)
    

def create(request):

    if request.method == "POST":
        # bila submit form

        #  print untuk lihat data yang dihantar
        print("Form data", request.POST)

        form = CreateTicketForm(request.POST)

        if form.is_valid():

            # get data from post request
            title = request.POST.get("title", "")
            description = request.POST.get("description", "")
            category_id = request.POST.get("category_id", "")
            department_id = request.POST.get("department_id", "")

            user = request.user
            department = Department.objects.get(id=department_id)
            category = Category.objects.get(id=category_id)

            # try create a new ticket
            Ticket.objects.create(
                title=title,
                description=description,
                user=user,
                department=department,
                category=category,
            )

    else:
        # bila papar form
        form = CreateTicketForm()

    # load additional data for the form
    departments = Department.objects.all()
    categories = Category.objects.all()

    context = {
        "departments": departments,
        "categories": categories,
        "form": form,
    }

    return render(request, "tickets/create.html", context)

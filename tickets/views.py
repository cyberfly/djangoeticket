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

    title = request.GET.get("title", "")
    category_id = request.GET.get("category_id", "")
    department_id = request.GET.get("department_id", "")

    if title:
        # filter tickets by id from category model
        tickets = tickets.filter(title__icontains=title)

    if category_id:
        # filter tickets by id from category model
        tickets = tickets.filter(category__id=category_id)

    if department_id:
        # filter tickets by id from department model
        tickets = tickets.filter(department__id=department_id)

    # initialize paginator
    page_size = 5
    paginator = Paginator(tickets, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # breakpoint()
    # end initialize paginator

    categories = Category.objects.all()
    departments = Department.objects.all()

    # breakpoint()
    context = {
        "page_obj": page_obj,
        "categories": categories,
        "departments": departments,
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

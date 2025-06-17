from django.shortcuts import render
from .models import Ticket
from lookups.models import Department, Category


# Create your views here.
def home(request):
    return render(request, "home.html")


def create(request):

    if request.method == "POST":
        # bila submit form

        #  print untuk lihat data yang dihantar
        print("Form data", request.POST)

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
        pass

    # load additional data for the form
    departments = Department.objects.all()
    categories = Category.objects.all()

    context = {
        "departments": departments,
        "categories": categories,
    }

    return render(request, "tickets/create.html", context)

from celery import shared_task
from django.core.mail import EmailMessage
from .models import Ticket

@shared_task
def add(x, y):
    """
    Quick test via shell_plus:
    >> from tickets.tasks import add
    >> add.delay(2, 3)
    """
    return x + y

@shared_task()
def send_new_ticket_email(ticket_id):

    ticket = Ticket.objects.get(id=ticket_id)

    email_body = f"""<h1>New Ticket Created</h1>
            
    <h3>Ticket Title: {ticket.title}</h3>
    <p>Ticket Description: {ticket.description}</p>
    <p>Category: {ticket.category.name}</p>
    <p>Department: {ticket.department.name}</p>
    <p>Status: {ticket.status}</p>
    <p>User: {ticket.user.username}</p>
    <p>Thank you for using our e-ticketing system.</p>
    <p>Best regards,</p>
    <p>E-Ticketing System</p>
    
    """

    email = EmailMessage(
        subject='New Ticket Created',
        body=email_body,
        from_email='system@eticketing.test',
        to=['admin@eticketing.test']
    )
    email.content_subtype = "html"
    email.send()
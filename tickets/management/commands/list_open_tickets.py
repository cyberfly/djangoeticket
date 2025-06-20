from django.core.management.base import BaseCommand
from tickets.models import Ticket

class Command(BaseCommand):
    help = 'List all open tickets'

    def handle(self, *args, **kwargs):
        tickets = Ticket.objects.filter(status='open')
        for ticket in tickets:
            self.stdout.write(f"ID: {ticket.id} | Title: {ticket.title} | User: {ticket.user}")
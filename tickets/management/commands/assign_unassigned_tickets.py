from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from tickets.models import Ticket

class Command(BaseCommand):
    help = 'Assign all unassigned tickets to a specified user'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int)

    def handle(self, *args, **options):
        user = get_user_model().objects.get(id=options['user_id'])
        tickets = Ticket.objects.filter(assignee__isnull=True)
        count = tickets.update(assignee=user)
        self.stdout.write(f"Assigned {count} unassigned tickets to {user.username}")
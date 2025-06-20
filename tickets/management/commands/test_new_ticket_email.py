from django.core.management.base import BaseCommand
from tickets.tasks import send_new_ticket_email

class Command(BaseCommand):
    help = 'Debug new ticket email'

    def add_arguments(self, parser):
        parser.add_argument('ticket_id', type=int)

    def handle(self, *args, **options):
        send_new_ticket_email.delay(options['ticket_id'])
        self.stdout.write(self.style.SUCCESS(f"Debugging email for ticket ID {options['ticket_id']}..."))
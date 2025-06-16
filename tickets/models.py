from django.db import models
from django.conf import settings

from lookups.models import Department, Category

class Ticket(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE,
        related_name='department_tickets',
    )

    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='category_tickets',
    )

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='open')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


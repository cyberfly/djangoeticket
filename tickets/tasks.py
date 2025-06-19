from celery import shared_task

@shared_task
def add(x, y):
    """
    Quick test via shell_plus:
    >> from tickets.tasks import add
    >> add.delay(2, 3)
    """
    return x + y
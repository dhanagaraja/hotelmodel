# your_app_name/tasks.py
from celery import shared_task
import remote_pdb
from . models import Booking


@shared_task
def add(x, y):
    models = Booking.objects.all()
    import ipdb; ipdb.set_trace()
    result = x + y
    return result
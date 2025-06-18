from itertools import chain
from django.conf import settings
from django.urls import resolve

def global_settings(request):
    return {
        "HELPSCOUT_BEACON_ID": '123',
    }
from django.conf import settings

def global_settings(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
    }
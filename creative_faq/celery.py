import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "creative_faq.settings")

app = Celery("creative_faq")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

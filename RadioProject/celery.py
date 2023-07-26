# import os
# from celery import Celery
# from datetime import timedelta
 
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RadioProject.settings')
# app = Celery('RadioProject')
# app.config_from_object('django.conf:settings', namespace='CELERY')
 
# app.conf.timezone = 'UTC'
 
# app.conf.beat_schedule = {
#     "add_first": {
#         "task": "manager.tasks.test_first",
#         "schedule": timedelta(seconds=3),
#     },
# }
 
# app.autodiscover_tasks()
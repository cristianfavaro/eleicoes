import os
from celery import Celery
from celery.schedules import crontab
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# #Configure manually tasks
# app.conf.beat_schedule = { # scheduler configuration   
#     ## Funds
#     'Funds Daily Report' : {  # whatever the name you want 
#         'task': 'funds.tasks.funds_daily_report_task', # name of task with path
#         'schedule': crontab(minute=30, hour=0),
#         'enabled': True, 
#         'args' : ["yesterday", "week"],
#         "description": "Dados para atualizar o daily report. Parâmetros: date (yyyymm) ou 'yesterday'; start_date: yyyy-mm-dd ou 'week' para pegar a última semana.",
#     },
#     'Funds Registration' : {  # whatever the name you want 
#         'task': 'funds.tasks.funds_registration_task', # name of task with path
#         'schedule': crontab(minute=10, hour=0),
#         'enabled': True, 
#         "description": "Atualiza a base de registro dos fundos.",
#     },
#     'Funds Documents Search' : {  
#         'task': 'funds.tasks.funds_documents', # name of task with path
#         'schedule': 300.0,
#         'enabled': not DEBUG, 
#         'args' : [False, False, False],
#         "description": "Atualiza os documentos. O parâmetro é data (dd/mm/YYYY, sem nada ele busca o dia atual) e paginate (default false. Para raspar todo o dia escrava '__all__'. ",
#     },
# }
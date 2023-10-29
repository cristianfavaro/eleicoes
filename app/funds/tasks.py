from celery import shared_task
from django.utils import timezone

@shared_task
def funds_documents(date=False, paginate=False, notify=False):
    from funds.parsers.documents import parse_data
    parse_data(
        date=date, 
        step = 100,
        paginate=paginate,
        notify=notify,
    )
    return 

@shared_task
def funds_daily_report_task(date, start_date):
    from funds.parsers.daily_data import parse_data
    if date == "yesterday":
        yesterday = timezone.now() - timezone.timedelta(days=1)
        date = f"{yesterday.year}{('0' + str(yesterday.month))[-2:]}"    

    if start_date == "week":
        start_date = timezone.now() - timezone.timedelta(days=7)
        
    response = parse_data(date=date, start_date=start_date)
    print(f"=={len(response)} files were parsed by daily report task.\n")
    return 

@shared_task
def funds_registration_task():
    from funds.parsers.funds import get_data
    get_data()
    print(f"==File was parsed by fund task.\n")
    return 

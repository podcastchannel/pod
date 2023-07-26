from django.shortcuts import render
from datetime import datetime,timedelta
from manager.models import Program,Announcement,LocalNew,GlobalNew

def home(request):
    program = Program.objects.order_by('start_date').first()
    context = {
        'now_program' : program,
        'next_program' : Program.objects.order_by('start_date')[1],
        'programs' : Program.objects.order_by('start_date')[1:4],
        'anns' : Announcement.objects.order_by('start_date')[:6],
        'local_news' : LocalNew.objects.order_by('start_date')[:4],
        'global_news' : GlobalNew.objects.order_by('start_date')[:4]
    }
    return render(request, 'home.html', context)


# from django_celery_beat.models import ClockedSchedule,PeriodicTask,CrontabSchedule
# from django.utils import timezone

def player(request):
    # date_obj = timezone.now()
    # crontab_schedule = CrontabSchedule.objects.create(minute=date_obj.minute + 1, 
    #                                                   hour=date_obj.hour, 
    #                                                   day_of_month=date_obj.day,
    #                                                   month_of_year=date_obj.month
    #                                                   )

    # task,created = PeriodicTask.objects.update_or_create(
    #                             name = 'notify_p1s',
    #                             defaults={
    #                                 'crontab' : crontab_schedule,
    #                                 'task' : 'manager.tasks.notify',
    #                                 'one_off' : False
    #                                 }
    #                             )


    
    # ClockedSchedule.objects.create(clocked_time=).save()

    return render(request, 'player.html')
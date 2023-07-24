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

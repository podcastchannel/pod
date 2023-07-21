from django.shortcuts import render
from datetime import datetime,timedelta
from manager.models import Program,Podcast,Blog,Competition

def home(request):
    program = Program.objects.order_by('start_date').first()
    context = {
        'program' : program,
        'programs' : Program.objects.order_by('start_date')[:4],
        'podcasts' : Podcast.objects.order_by('start_date')[:4],
        'competitions' : Competition.objects.order_by('start_date')[:4],
        'blogs' : Blog.objects.order_by('start_date')[:12]
    }
    return render(request, 'home.html', context)

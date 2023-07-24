from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Program,Announcement,LocalNew,GlobalNew
import json


def dashboard(request):
    context = {
        'programs': Program.objects.all()[:4],
        'program_count': Program.objects.count(),
        'anns' : Announcement.objects.all()[:5],
        'ann_count': Announcement.objects.count(),
        'global_news' : GlobalNew.objects.all()[:5],
        'global_news_count': GlobalNew.objects.count(),
        'local_news' : LocalNew.objects.all()[:5],
        'local_news_count': LocalNew.objects.count(),
    }
    return render(request, 'dashboard.html', context)


def fix_obj_1(obj, item):
    obj['id'] = item.id
    obj['name'] = item.name
    obj['description'] = item.description
    obj['start_date'] = item.start_date.strftime('%Y-%m-%d %H:%M:%S')
    obj['end_date'] = item.end_date.strftime('%Y-%m-%d %H:%M:%S')
    obj['image_url'] = item.thumb.url


def create_program(request, program):
    prog_day = int(request.POST.get('py_day'))
    current_date = datetime.today()
    days_to = (prog_day - current_date.weekday()) % 7
    prog_date = (current_date + timedelta(days=days_to)).strftime('%Y-%m-%d %H:%M:%S')

    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')

    program.name = request.POST.get('name').upper()
    program.description = request.POST.get('description')
    program.start_date = datetime.strptime(prog_date.split(' ')[0] + f' {start_time}', "%Y-%m-%d %H:%M")
    program.end_date = datetime.strptime(prog_date.split(' ')[0] + f' {end_time}', "%Y-%m-%d %H:%M")
    
    if request.POST.get('one_off'):
        program.one_off = True
    else:
        program.one_off = False

def programs(request):
    program_list = []
    for program in Program.objects.order_by('start_date'):
        program_obj = {}
        fix_obj_1(program_obj, program)
        program_obj['one_off'] = program.one_off
        program_list.append(program_obj)

    if request.method == 'POST':
        if request.POST.get('id'):
            program = Program.objects.get(id=request.POST.get('id'))
            if request.FILES:
                program.thumb = request.FILES['image']
        else:
            program = Program()
            program.thumb = request.FILES['image']
        
        create_program(request, program)
        program.save()
        return redirect('programs_page')
    
    context = {
        'token' : get_token(request),
        'program_list': json.dumps(program_list),
    }
    return render(request, 'programs.html', context)

def delete_program(request):
    json_data = json.loads(request.body)['data']
    Program.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'del_program'})


def fix_obj_2(obj, item):
    obj['id'] = item.id
    obj['name'] = item.name
    obj['description'] = item.description
    obj['start_date'] = item.start_date.strftime('%Y-%m-%d %H:%M:%S')
    obj['image_url'] = item.thumb.url
    obj['share_link'] = item.share_link
    obj['social_accounts'] = item.social_accounts

def create_program_2(request, obj):
    if request.POST.get('id'):
        program = obj.objects.get(id=request.POST.get('id'))
        if 'image' in request.FILES:
            program.thumb = request.FILES['image']
    else:
        program = obj()
        program.thumb = request.FILES['image']
    program.name = request.POST.get('name').upper()
    program.description = request.POST.get('description')
    if request.POST.get('share_link'):
        program.share_link = request.POST.get('share_link')
    if request.POST.get('social_accounts'):
        program.social_accounts = request.POST.get('social_accounts')
    program.save()

def announcements(request):
    program_list = []
    for program in Announcement.objects.order_by('start_date'):
        program_obj = {}
        fix_obj_2(program_obj, program)
        program_list.append(program_obj)

    if request.method == 'POST':
        create_program_2(request, Announcement)
        return redirect('announcements_page')
    context = {
        'token' : get_token(request),
        'program_list': json.dumps(program_list),
    }
    return render(request, 'announcements.html', context)

def delete_announcement(request):
    json_data = json.loads(request.body)['data']
    Announcement.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'del_pod'})

def local_news(request):
    program_list = []
    for program in LocalNew.objects.order_by('start_date'):
        program_obj = {}
        fix_obj_2(program_obj, program)
        program_list.append(program_obj)

    if request.method == 'POST':
        create_program_2(request, LocalNew)
        return redirect('local_news_page')
    context = {
        'token' : get_token(request),
        'program_list': json.dumps(program_list),
    }
    return render(request, 'local_news.html', context)

def delete_local_news(request):
    json_data = json.loads(request.body)['data']
    LocalNew.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'del_pod'})

def global_news(request):
    program_list = []
    for program in GlobalNew.objects.order_by('start_date'):
        program_obj = {}
        fix_obj_2(program_obj, program)
        program_list.append(program_obj)

    if request.method == 'POST':
        create_program_2(request, GlobalNew)
        return redirect('global_news_page')
    context = {
        'token' : get_token(request),
        'program_list': json.dumps(program_list),
    }
    return render(request, 'global_news.html', context)

def delete_global_news(request):
    json_data = json.loads(request.body)['data']
    GlobalNew.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'del_pod'})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def now_playing(request):
    return render(request, 'now_playing.html')

@csrf_exempt
def now_playing_php(request):
    return render(request, 'now_playing.php')

@csrf_exempt
def now_playing_txt(request):
    return render(request, 'now_playing.txt')

@csrf_exempt
def play(request):
    if request.method == 'POST':
        line = request.POST
    else:
        line = 'Omar'
    context ={
        'line' : line
    }
    return render(request, 'play.html', context)





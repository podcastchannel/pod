from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Program,Podcast,Blog,Competition
import json


def dashboard(request):
    context = {
        'programs': Program.objects.all()[:4],
        'program_count': Program.objects.count(),
        'podcasts' : Podcast.objects.all()[:5],
        'podcast_count': Podcast.objects.count(),
        'competitions' : Competition.objects.all()[:5],
        'competition_count': Competition.objects.count(),
        'blogs' : Blog.objects.all()[:5],
        'blog_count' : Blog.objects.count()
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

def podcasts(request):
    program_list = []
    for program in Podcast.objects.order_by('start_date'):
        program_obj = {}
        fix_obj_1(program_obj, program)
        program_obj['one_off'] = program.one_off
        program_obj['audio'] = program.audio.url
        program_list.append(program_obj)

    if request.method == 'POST':
        if request.POST.get('id'):
            program = Podcast.objects.get(id=request.POST.get('id'))
            if 'image' in request.FILES:
                program.thumb = request.FILES['image']
            if 'audio' in request.FILES:
                program.audio = request.FILES['audio']
        else:
            program = Podcast()
            program.thumb = request.FILES['image']
            program.audio = request.FILES['audio']

        create_program(request, program)
        program.save()
        return redirect('podcasts_page')
    context = {
        'token' : get_token(request),
        'program_list': json.dumps(program_list),
    }
    return render(request, 'podcasts.html', context)

def delete_podcast(request):
    json_data = json.loads(request.body)['data']
    Podcast.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'del_pod'})


def fix_obj_2(obj, item):
    obj['id'] = item.id
    obj['name'] = item.name
    obj['description'] = item.description
    obj['start_date'] = item.start_date.strftime('%Y-%m-%d %H:%M:%S')
    obj['image_url'] = item.thumb.url
    obj['share_link'] = item.share_link
    obj['social_accounts'] = item.social_accounts

def create_program_2(request, program):
    program.name = request.POST.get('name').upper()
    program.description = request.POST.get('description')
    if request.POST.get('share_link'):
        program.share_link = request.POST.get('share_link')
    if request.POST.get('social_accounts'):
        program.social_accounts = request.POST.get('social_accounts')

def blogs(request):
    program_list = []
    for program in Blog.objects.order_by('start_date'):
        program_obj = {}
        fix_obj_2(program_obj, program)
        program_obj['share_link'] = program.share_link
        program_obj['social_accounts'] = program.social_accounts
        program_list.append(program_obj)
    if request.method == 'POST':
        if request.POST.get('id'):
            if request.POST.get('id'):
                program = Blog.objects.get(id=request.POST.get('id'))
                if request.FILES:
                    program.thumb = request.FILES['image']
        else:
            program = Blog()
            program.thumb = request.FILES['image']
            program.start_date = datetime.today()
        create_program_2(request, program)
        program.save()
        return redirect('blogs_page')
    context = {
        'token' : get_token(request),
        'program_list': json.dumps(program_list),
    }
    return render(request, 'blogs.html', context)

def delete_blog(request):
    json_data = json.loads(request.body)['data']
    Blog.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'del_blog'})

def competitions(request):
    program_list = []
    for program in Competition.objects.order_by('start_date'):
        program_obj = {}
        fix_obj_2(program_obj, program)
        
        program_obj['end_date'] = program.end_date.strftime('%Y-%m-%d %H:%M:%S')
        program_obj['days_left'] = (program.start_date - timezone.now()).days
        program_list.append(program_obj)
    if request.method == 'POST':
        if request.POST.get('id'):
            if request.POST.get('id'):
                program = Competition.objects.get(id=request.POST.get('id'))
                if request.FILES:
                    program.thumb = request.FILES['image']
        else:
            program = Competition()
            program.thumb = request.FILES['image']
        create_program_2(request, program)
        program.start_date = request.POST.get('start_time')
        program.end_date = request.POST.get('end_time')
        program.save()
        return redirect('competitions_page')
    context = {
        'token' : get_token(request),
        'program_list': json.dumps(program_list),
    }
    return render(request, 'competitions.html', context)

def delete_competition(request):
    json_data = json.loads(request.body)['data']
    Competition.objects.get(id=int(json_data)).delete()
    return JsonResponse({'test':'del_competition'})


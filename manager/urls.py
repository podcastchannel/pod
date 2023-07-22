from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard_page'),
    
    path('programs', views.programs, name='programs_page'),
    path('delete_program', views.delete_program),

    path('announcements', views.announcements, name='announcements_page'),
    path('delete_announcement', views.delete_announcement),

    path('local_news', views.local_news, name='local_news_page'),
    path('delete_local_news', views.delete_local_news),

    path('global_news', views.global_news, name='global_news_page'),
    path('delete_global_news', views.delete_global_news),
]
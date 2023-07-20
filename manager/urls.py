from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard_page'),
    
    path('programs', views.programs, name='programs_page'),
    path('delete_program', views.delete_program),

    path('podcasts', views.podcasts, name='podcasts_page'),
    path('delete_podcast', views.delete_podcast),

    path('blogs', views.blogs, name='blogs_page'),
    path('delete_blog', views.delete_blog),

    path('competitions', views.competitions, name='competitions_page'),
    path('delete_competition', views.delete_competition),
]
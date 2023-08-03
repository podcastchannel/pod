from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),

    path('player', views.player, name='player_page'),
    path('view_local_news/<str:slug>/', views.view_local_news, name='view_local_news_page'),

    path('terms', views.terms, name='terms_page'),
]
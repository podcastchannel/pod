from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('player', views.player, name='player_page'),
]
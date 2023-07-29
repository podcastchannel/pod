from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    

    path('player', views.player, name='player_page'),

    path('terms', views.terms, name='terms_page'),
]
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', base, name='home'),
    path('msk/', msk, name='msk'),
    path('spb/', spb, name='spb'),
    path('nsk/', nsk, name='nsk'),
    path('ekb/', ekb, name='ekb'),
    path('kazan/', kazan, name='kazan'),
    path('cards/<int:cards_id>/', TourView, name='cards'),

]


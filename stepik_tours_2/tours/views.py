from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

citys = [{'title': 'Из Москвы', 'url_name': 'msk'},
         {'title': 'Из Петербурга', 'url_name': 'spb'},
         {'title': 'Из Новосибирска', 'url_name': 'nsk'},
         {'title': 'Из Екатеринбурга', 'url_name': 'ekb'},
         {'title': 'Из Казани', 'url_name': 'kazan'}]

def base(request):
    card = Cards.objects.all()
    context = {'card': card,
               'citys': citys,
               'title': 'Stepik Tours',
               'cit_selected': 0,
               }
    return render(request, 'tours/base.html', context=context)

def msk(request):
    return render(request, 'tours/msk.html', {'citys': citys, 'title': 'Stepik Tours'})

def spb(request):
    return render(request, 'tours/spb.html', {'citys': citys, 'title': 'Stepik Tours'})

def nsk(request):
    return render(request, 'tours/nsk.html', {'citys': citys, 'title': 'Stepik Tours'})

def ekb(request):
    return render(request, 'tours/ekb.html', {'citys': citys, 'title': 'Stepik Tours'})

def kazan(request):
    return render(request, 'tours/kazan.html', {'citys': citys, 'title': 'Stepik Tours'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def TourView(request, cards_id):
    return HttpResponse(f'отображение тура с id = {cards_id}')




# Create your views here.

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View
import tours.data as dat


def main_view(request):
    return render(request, 'main.html', {'title': dat.title, 'subtitle': dat.subtitle, 'description': dat.description,'departures': dat.departures, 'tours': dat.tours})

def departure_view(request,departure):
    dep=dat.departures[departure]
    if not departure:
        return HttpResponseNotFound(f"Нет направления {departure}")
    return render(request, "departure.html", {'dep':dep, 'title': dat.title, 'departures': dat.departures, 'tours':dat.tours, 'depart':departure})

def tour_view(request,id):
    if not id:
        return HttpResponseNotFound(f"Нет тура с номером {id}")
    tour=dat.tours[id]
    return render(request, "tour.html", {'title': dat.title, 'departures': dat.departures, 'tour': tour})

class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html', {'name': 'Alex', 'place': 'Lab'})



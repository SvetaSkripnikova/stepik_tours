# Create your views here.

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View


def main_view(request):
    return render(request, "main.html")

def departure_view(request,departure):
    if not departure:
        return HttpResponseNotFound(f"Нет направления {departure}")
    return render(request, "departure.html", context='')

def tour_view(request,id):
    if not id:
        return HttpResponseNotFound(f"Нет тура с номером {id}")
    return render(request, "tour.html", context='')

class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html', {'name': 'Alex', 'place': 'Lab'})



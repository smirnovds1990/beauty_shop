# from django.http import HttpResponse
from django.shortcuts import render

from .models import Master, Procedure


def index(request):
    'Контент стартовой страницы.'
    template = 'registration/index.html'
    return render(request, template)


def get_masters(request):
    'Контент страницы выбора специалиста.'
    masters = Master.objects.all()
    context = {'masters': masters}
    template = 'registration/masters.html'
    return render(request, template, context)


def get_procedures(request):
    'Контент страницы выбора процедуры.'
    procedures = Procedure.objects.all()
    context = {'procedures': procedures}
    template = 'registration/procedures.html'
    return render(request, template, context)

# from django.http import HttpResponse
from django.shortcuts import render

from .models import Master, Procedure


def index(request):
    template = 'registration/index.html'
    return render(request, template)


def get_masters(request):
    masters = Master.objects.all()
    context = {'masters': masters}
    template = 'registration/masters.html'
    return render(request, template, context)


def get_procedures(request):
    procedures = Procedure.objects.all()
    context = {'procedures': procedures}
    template = 'registration/procedures.html'
    return render(request, template, context)

# from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import MasterForm, ProcedureForm, RecordForm
from .models import Customer, Master, Procedure, Record


def index(request):
    """Контент стартовой страницы."""
    template = 'registration/index.html'
    return render(request, template)


def get_masters(request):
    """Контент страницы выбора специалиста."""
    template = 'registration/masters.html'
    masters = Master.objects.all()
    procedures = Procedure.objects.all()
    form = ProcedureForm()
    context = {
        'masters': masters,
        'procedures': procedures,
        'form': form
    }
    return render(request, template, context)


def get_procedures(request):
    """Контент страницы выбора процедуры."""
    procedures = Procedure.objects.all()
    context = {'procedures': procedures}
    template = 'registration/procedures.html'
    return render(request, template, context)


def new_record(request):
    """Создание новой записи."""
    template = 'registration/new_record.html'
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration:finished_record')
    else:
        form = RecordForm()
    return render(request, template, {'form': form})


def finished_record(request):
    """Страница подтверждения отправки данных записи."""
    template = 'registration/finished_record.html'
    return render(request, template)

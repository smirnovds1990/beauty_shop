from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from .models import Master, Procedure, Record


class MasterForm(forms.ModelForm):
    # masters = Master.objects.all()
    date = forms.DateTimeField(
        label='Выберите дату и время', widget=DateTimePickerInput()
    )
    # master = forms.ChoiceField(
    #     choices=[
    #         (Master.objects.get(name='Татьяна Смирнова'), 'Татьяна Смирнова'),
    #         (Master.objects.get(name='Елена Груздева'), 'Елена Груздева'),
    #     ],
    #     required=True,
    #     label='Выберите специалиста'
    # )

    class Meta:
        model = Master
        fields = ('name',)


class ProcedureForm(forms.ModelForm):
    date = forms.DateTimeField(
        label='Выберите дату и время', widget=DateTimePickerInput()
    )

    class Meta:
        model = Procedure
        fields = ('master', 'title')


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('date', 'master', 'procedure', 'customer')
        # widgets = {
        #     'date': DateTimePickerInput(),
        # }

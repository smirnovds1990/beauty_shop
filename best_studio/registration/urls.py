from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.new_record, name='new_record'),
    path('finished_record/', views.finished_record, name='finished_record'),
    path('registration/', views.index, name='index'),
    path('masters/', views.get_masters, name='masters'),
    path('procedures/', views.get_procedures, name='procedures'),
]

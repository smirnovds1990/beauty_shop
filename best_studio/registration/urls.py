from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.index, name='index'),
    path('masters/', views.get_masters, name='masters'),
    path('procedures/', views.get_procedures, name='procedures'),
]

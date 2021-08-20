from django.urls import path

from . import views

app_name = 'lmmCalc'

urlpatterns = [
    path('', views.index, name='index'),
    path('answer', views.answer, name='answer')
]
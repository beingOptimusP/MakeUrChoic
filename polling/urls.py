from django.contrib import admin
from django.urls import path,include
from polling import views

urlpatterns = [
    path('',views.index,name='home'),
    path('create',views.create,name='create'),
    path('CreatePoll/<poll_id>/',views.CreatePoll,name='poll'),
    path('pollResult/<poll_id>/',views.pollResult,name='result'),
    path('Tpolls',views.Tpolls,name='Tpolls'),
    path('Teams',views.Teams,name="Team"),
    path('Openpoll/<poll_id>/',views.OpenPoll,name='open')
]
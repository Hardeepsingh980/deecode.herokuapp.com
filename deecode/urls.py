from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('app/',views.sendHumkam, name='send-hukam'),
    path('app/2',views.sendGurupurab, name='send-gurupurab'),
]

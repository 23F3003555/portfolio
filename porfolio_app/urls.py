from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='home'),

    path('contect/',views.contect,name="contect")
]
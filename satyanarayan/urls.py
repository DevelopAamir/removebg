from django.urls import path, include
from satyanarayan import views

urlpatterns = [
    path('', views.index, name='home'),
    path('removebg', views.removebg, name='removebg'),
]
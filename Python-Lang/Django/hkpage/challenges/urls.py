from django.urls import path
from . import views

urlpatterns = [
    path("day1", views.trigger1),
    path("day2",views.trigger2),
    path("day3",views.trigger3),
    path("day4",views.trigger4,name='trigger4')
]
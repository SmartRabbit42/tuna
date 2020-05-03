from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_fish', views.add_fish, name='add_fish'),
]

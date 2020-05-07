from django.urls import path
from . import views

app_name = 'shoal'

urlpatterns = [
    # /shoal/
    path('', views.index, name='index'),

    # /shoal/<shoal_id>/
    path('<int:shoal_id>/', views.shoal, name='shoal'),

    # /shoal/join/
    path('join/', views.join, name='join'),

    # /shoal/create/
    path('create/', views.create, name='create'),

    # /shoal/add/
    path('add/', views.ShoalCreate.as_view(), name='shoal-add'),
]

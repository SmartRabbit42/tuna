from django.urls import path
from . import views

urlpatterns = [
    # /shoal/
    path('', views.index, name='index'),

    # /shoal/48163264/
    path('<int:shoal_id>/', views.shoal, name='shoal'),
]

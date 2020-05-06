from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoal, Fish

def index(request):
    return render(request, 'shoal/index.html')

def shoal(request, shoal_id):
    shoal = get_object_or_404(Shoal, id=shoal_id)
    return render(request, 'shoal/shoal.html', context = { 'shoal': shoal })

def create(request):
    shoal_name = request.POST['shoal_name']
    shoal = Shoal(name=shoal_name)
    shoal.save()
    return redirect('shoal:shoal', shoal_id=shoal.id)

def join(request):
    shoal_id = request.POST['shoal_id']
    return redirect('shoal:shoal', shoal_id)

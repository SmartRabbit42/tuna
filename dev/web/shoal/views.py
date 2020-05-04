from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shoal, Fish

def index(request):
    if(request.GET.get('join')):
      shoal_id = request.GET.get('shoal_id')

      if Shoal.objects.filter(id=shoal_id):
          return redirect('/shoal/{0}/'.format(shoal_id))

    if(request.GET.get('create')):
        shoal_name = request.GET.get('shoal_name')
        new_shoal = Shoal(name=shoal_name)
        new_shoal.save()

        return redirect('/shoal/{0}/'.format(new_shoal.id))

    return render(request, 'shoal/index.html')

def shoal(request, shoal_id):
    this_shoal = Shoal.objects.filter(id = shoal_id)
    context = {}
    if (this_shoal):
        fishs = Fish.objects.filter(shoal = shoal_id)
        context = {
            'shoal_name': this_shoal[0].name,
            'shoal_description': this_shoal[0].description,
            'fishs': fishs,
        }
    return render(request, 'shoal/shoal.html', context)

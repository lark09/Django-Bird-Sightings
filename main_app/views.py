from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Bird, Location
from .forms import SightingForm

def assoc_location(request, bird_id, location_id):
    bird = Bird.object.get(id=bird_id)
    bird.locations.add(location_id)
    return redirect ('detail', bird_id=bird_id)

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'
    success_url = '/birds/'


class BirdUpdate(UpdateView):
    model = Bird
    fields = ['name', 'family', 'description', 'age']
    # redirect is happening by the get_absolute_url defined on the model


class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'


def add_sighting(request, bird_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.bird_id = bird_id
        new_sighting.save()
    return redirect('detail', bird_id=bird_id)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})


def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    sighting_form = SightingForm()
    return render(request, 'birds/detail.html', {'bird': bird, 'sighting_form': sighting_form})

class LocationList(ListView):
  model = Location

class LocationDetail(DetailView):
  model = Location

class LocationCreate(CreateView):
  model = Location
  fields = '__all__'

class LocationUpdate(UpdateView):
  model = Location
  fields = ['name', 'weather']

class LocationDelete(DeleteView):
  model = Location
  success_url = '/locations/'
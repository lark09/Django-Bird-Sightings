from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'
    success_url = '/birds/'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['name','family', 'description', 'age']
    # redirect is happening by the get_absolute_url defined on the model


class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'
    
def home(request):
    return HttpResponse('<h1> Heyo Birder </h1>')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html',{ 'bird': bird })
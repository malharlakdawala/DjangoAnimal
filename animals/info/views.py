import json

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Person

# Create your views here.

def family(request,id):
    with open('data.json') as f:
        data = json.load(f)
    selected_animal=[]
    for animal in data['animals']:
        if animal['family']==id:
            selected_animal.append(animal)
            print(selected_animal)
    return render(request,'family.html',{'animal':selected_animal})


def animal(request, id):
    with open('data.json') as f:
        data = json.load(f)
    selected_family = None
    for family in data['families']:
        if family['id'] == id:
            selected_family=family
            return render(request, 'animal.html', {'family': selected_family})

def animals(request):
    with open('data.json') as f:
        data = json.load(f)
        animal_name=[]
    for animal in data['animals']:
        animal_name.append(animal["name"])
    return render(request, 'animal_name.html',{'animal_name':animal_name})

def person_view(request,id):
    peep=Person.objects.get(id=person_id)
    return render(request,'animal.html',{'person':peep})
import json

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def family(request,id):
#     with open('data.json') as f:
#         data = json.load(f)
#     selected_family=None
#     for family in data['families']:
#         if family['id']==id:
#             selected_family=family
#     return render(request,'family.html',{'family':selected_family})

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
    selected_animal = None
    for animal in data['animals']:
        if animal['id'] == id:
            selected_animal = animal
    return render(request, 'animal.html', {'animal': selected_animal})

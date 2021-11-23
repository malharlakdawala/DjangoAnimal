from django.shortcuts import render
from .models import *

# Create your views here.
def persons_phonenumber(request,phonenumber):
    person= MyModel.objects.get(phone_number=phonenumber)
    return render(request, 'person.html', {'person': person})

def persons_name(request,name_str):
    person = MyModel.objects.get(name=name_str)
    return render(request, 'person.html', {'person': person})

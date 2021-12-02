import random

from django.shortcuts import render
from .models import *
from faker import Faker
from django.http import HttpResponse
from .forms import *
import random


# Create your views here.

def add_data(request, id):
    f = Faker()

    for i in range(1, id):
        first_name = f.first_name()
        last_name = f.last_name()
        email = f.email()
        phonenumber = random.randint(9111111111, 9999999999)
        address = f.address()
        city = f.city()
        country = f.country()
        Customer.objects.create(first_name=first_name, last_name=last_name, email=email, phonenumber=phonenumber,
                                address=address, city=city, country=country)
    return HttpResponse('')


def add_rental_data(request, id):
    f = Faker()

    for _ in range(id):
        rental_date = f.date_between(start_date='-30d', end_date='today')
        return_date = random.choice([None, (f.date_between(start_date=rental_date, end_date='today'))])
        # customer=Customer.objects.get(id=random.randint(1,100))
        # vehicle=Vehicle.objects.get(id=random.randint(0,15))
        customer_id=random.randint(1,100)
        vehicle_id=random.randint(1,15)
        print("this is getting inserted ",rental_date,return_date,customer_id,vehicle_id)

        Rental.objects.create(rental_date=rental_date,return_date=return_date,customer_id=customer_id,vehicle_id=vehicle_id)
    return HttpResponse('')

def home(request):
    return render(request, 'dashboard.html')

def all_rental(request):

    rental_details=Rental.objects.filter(return_date=None).order_by("rental_date")
    return render(request, 'rental/all_rental.html',{'rental_details':rental_details})

def single_rental(request,id):
    rental_details = Rental.objects.get(id=id)
    return render(request, 'rental/single_rental.html',{'rental_details':rental_details})


def add_rental(request):
    context={
        'page_title':"Add Rental",
        'form':Add_rental
    }
    if request.method == "POST":
        form = Add_rental(request.POST)
        print("data", form.data)
        if form.is_valid():
            rental_date = form.cleaned_data['rental_date']
            return_date = form.cleaned_data['return_date']
            customer = form.cleaned_data['customer']
            vehicle = form.cleaned_data['vehicle']
            context['formInfo'] = {
                'rental_date': rental_date,
                'return_date': return_date,
                'customer': customer,
                'vehicle': vehicle
            }
            # context['btnFormHidden'] = True  # To hide the button is the form is successfully submitted
            # print the values to make sure their are correct
            print(context['formInfo'])
            print("cleaned data form is: ", form.cleaned_data)
            rental = Rental.objects.create(**form.cleaned_data)
            return render(request,'success.html')
            #return render(request, 'rental/add_rental.html', {'rental': Rental.objects.get(id=rental.id)})
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'add_rental.html', context)
    else:
        # GET, generate blank form
        context['form'] = Add_rental()
    return render(request, 'rental/add_rental.html', context)



def all_customer(request):
    pass

def single_customer(request,id):
    pass

def add_customer(request):
    pass

def all_vehicle(request):
    pass

def single_vehicle(request,id):
    pass

def add_vehicle(request):
    pass


#Customer.objects.all().order_by("first_name")




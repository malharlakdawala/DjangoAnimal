import random

from django.shortcuts import render
from .forms import Search_form
from .models import CompanyRecords
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import re
from pyindia_zipcode import ZipCode



# Create your views here.

def search(request):
    if not request.method == "POST" and 'page' in request.GET:
        if 'search-query' in request.session:
            request.POST = request.session['search-query']
            request.method = 'POST'

    if request.method == 'POST':
        form = Search_form(request.POST)
        request.session['search-query'] = request.POST
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            search_parameter = form.cleaned_data.get('search_parameter')
            if re.match('^[1-9][0-9]{5}$',search_query):
                pincode_detais=more_details(search_query)
            else:
                pincode_detais={}
            print(search_query, search_parameter)
            # queryset_list = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
            #     company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(
            #     emails__isnull=True).exclude(contact_person__isnull=True)[:100]
            queryset_list = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
                company_name__isnull=True).exclude(description__isnull=True)[:100]
            page = request.GET.get('page', 1)
            paginator = Paginator(queryset_list, 6)

            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                queryset = paginator.page(1)
            except EmptyPage:
                queryset = paginator.page(paginator.num_pages)
            form = Search_form()
            gmap_array = []
            for query in queryset:
                address = query.company_name + " " + query.address
                address = re.sub(r'[^A-Za-z0-9 ]+', ' ', address)
                gmap_array.append(address)
            gmap_array = json.dumps(gmap_array)
            return render(request, 'search/search_results.html',
                          {'queryset': queryset, 'form': form, 'gmap_array': gmap_array,'search_query':search_query,'pincode_detais':pincode_detais})

    else:
        context = {
            'form': Search_form()
        }
        return render(request, 'search/search.html', context)


def more_details(pincode):
    obj = ZipCode()
    pincode_response = obj.get_zipcode_info(pincode)
    pincode_response = pincode_response[0]

    population = random.randint(20000,100000)
    male_population = int(0.53*population)
    female_population = int(0.47*population)
    avg_income = random.randint(10000,20000)
    socities = int(population/(450))
    spending_capacity = int(avg_income*0.43)
    life_quality = random.randint(1,100)


    restaurants = int(population/500)
    educational_institutes = int(population/4000)
    temples = int(population/1000)
    theaters = int(population/8000)
    hospitals = int(population/10000)
    kirana = int(population/1000)
    banks = int(population/1200)
    parks = int(population/12000)
    offices = int(population/850)

    statistics = {
        "population":population,
        "male_population":male_population,
        "female_population":female_population,
        "avg_income":avg_income,
        "restaurants":restaurants,
        "educational_institutes":educational_institutes,
        "temples":temples,
        "theaters":theaters,
        "hospitals":hospitals,
        "kirana":kirana,
        "banks":banks,
        "parks":parks,
        "socities":socities,
        "spending_capacity":spending_capacity,
        "life_quality":life_quality,
        "offices":offices,

    }

    pincode_detais ={
        "pincode_response" : pincode_response,
        "statistics":statistics,
    }
    return pincode_detais
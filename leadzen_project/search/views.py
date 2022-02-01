import random

from django.shortcuts import render
from .forms import Search_form
from .models import CompanyRecords, DataStorage, ExcelUpload
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import re
from pyindia_zipcode import ZipCode
from search.forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import pandas as pd

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage


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
            if re.match('^[1-9][0-9]{5}$', search_query):
                pincode_detais = more_details(search_query)
            else:
                pincode_detais = {}
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
                          {'queryset': queryset, 'form': form, 'gmap_array': gmap_array, 'search_query': search_query,
                           'pincode_detais': pincode_detais})

    else:
        context = {
            'form': Search_form()
        }
        return render(request, 'search/search.html', context)


def more_details(pincode):
    obj = ZipCode()
    pincode_response = obj.get_zipcode_info(pincode)
    pincode_response = pincode_response[0]

    population = random.randint(20000, 100000)
    male_population = int(0.53 * population)
    female_population = int(0.47 * population)
    avg_income = random.randint(10000, 20000)
    socities = int(population / (450))
    spending_capacity = int(avg_income * 0.43)
    life_quality = random.randint(1, 100)

    restaurants = int(population / 500)
    educational_institutes = int(population / 4000)
    temples = int(population / 1000)
    theaters = int(population / 8000)
    hospitals = int(population / 10000)
    kirana = int(population / 1000)
    banks = int(population / 1200)
    parks = int(population / 12000)
    offices = int(population / 850)

    statistics = {
        "population": population,
        "male_population": male_population,
        "female_population": female_population,
        "avg_income": avg_income,
        "restaurants": restaurants,
        "educational_institutes": educational_institutes,
        "temples": temples,
        "theaters": theaters,
        "hospitals": hospitals,
        "kirana": kirana,
        "banks": banks,
        "parks": parks,
        "socities": socities,
        "spending_capacity": spending_capacity,
        "life_quality": life_quality,
        "offices": offices,

    }

    pincode_detais = {
        "pincode_response": pincode_response,
        "statistics": statistics,
    }
    return pincode_detais


def geocode(name_address):
    url = "https://google-maps-geocoding-plus.p.rapidapi.com/geocode"

    querystring = {"address": name_address, "language": "en"}

    headers = {
        'x-rapidapi-host': "google-maps-geocoding-plus.p.rapidapi.com",
        'x-rapidapi-key': "d6a2e73179mshfa5a8a3fa183d90p1a1499jsn14c184f39007"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


class ExportImportExcel(APIView):
    def post(self, request):
        temp_arr = []
        excel_upload_obj = ExcelUpload.objects.create(excel_file_upload=request.FILES['files'])
        df = pd.read_csv(f"{settings.BASE_DIR}/{excel_upload_obj.excel_file_upload}")
        # print(df)
        for data in df.values.tolist():
            geocode_json = geocode(data[4] + ", " + data[8])
            print(geocode_json)

            # DataStorage.objects.create(
            #     title=data[4],
            #     full_address=
            #     area
            # address1
            # city
            # state
            # pincode
            # country
            # phone_number
            # place_type
            # industry
            # website
            # social_links
            # price_range
            # timing
            # thumbnail
            #
            # latitude
            # longitude
            #
            # google_place_id
            # place_link
            # cid
            # reviews_link
            # booking_link
            # place_id
            # global_plus_code
            # compound_plus_code
            # review_count
            # rating
            # createdate
            # modifieddate

            # )
        return Response({'status': 200})

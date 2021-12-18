from django.shortcuts import render
from .forms import Search_form
from .models import CompanyRecords
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import re


# Create your views here.

def search(request):
    if not request.method == "POST" and 'page' in request.GET:
        if 'search-query' in request.session:
            request.POST = request.session['search-query']
            request.method = 'POST'

    if request.method == 'POST':
        form = Search_form(request.POST)
        # request.session['search-query'] = request.POST
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            search_parameter = form.cleaned_data.get('search_parameter')
            print(search_query, search_parameter)
            queryset_list = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
                company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(
                emails__isnull=True).exclude(contact_person__isnull=True)[:100]
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
                          {'queryset': queryset, 'form': form, 'gmap_array': gmap_array,'search_query':search_query})

    else:
        context = {
            'form': Search_form()
        }
        return render(request, 'search/search.html', context)

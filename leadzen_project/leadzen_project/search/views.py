from django.shortcuts import render
from .forms import Search_form
from .models import CompanyRecords
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests


# Create your views here.

# def search1(request):
#     context = {
#         'form': Search_form()
#     }
#     if request.method == 'POST':
#         form = Search_form(request.POST)
#         if form.is_valid():
#             search_query = form.cleaned_data.get('search_query')
#             search_parameter = form.cleaned_data.get('search_parameter')
#             print(search_query, search_parameter)
#             queryset_list = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
#                 company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(
#                 emails__isnull=True)[:5]
#             page = request.GET.get('page', 1)
#             paginator = Paginator(queryset_list, 2)
#
#             try:
#                 queryset = paginator.page(page)
#             except PageNotAnInteger:
#                 queryset = paginator.page(1)
#             except EmptyPage:
#                 queryset = paginator.page(paginator.num_pages)
#         return render(request,'search/search.html',{"queryset":queryset})
#     if request.method == 'GET':
#         if 'queryset' in request.session:
#             queryset_list = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
#                 company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(
#                 emails__isnull=True)[:5]
#             page = request.GET.get('page', 1)
#             paginator = Paginator(queryset_list, 2)
#
#             try:
#                 queryset = paginator.page(page)
#             except PageNotAnInteger:
#                 queryset = paginator.page(1)
#             except EmptyPage:
#                 queryset = paginator.page(paginator.num_pages)
#         return render(request,'search/search.html',{"queryset":queryset})
#
#     return render(request, 'search/search.html', context)
#
#
# def show_data(request, search_query, search_parameter):
#     queryset_list = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
#         company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(
#         emails__isnull=True)[:5]
#     page = 1
#     page = request.GET.get('page', 1)
#     paginator = Paginator(queryset_list, 2)
#
#     try:
#         queryset = paginator.page(page)
#     except PageNotAnInteger:
#         queryset = paginator.page(1)
#     except EmptyPage:
#         queryset = paginator.page(paginator.num_pages)
#
#     return render_to_response('search/search_results.html', {'queryset': queryset})

# def search(request):
#     context = {
#         'form': Search_form()
#     }
#     if request.method == 'POST':
#         form = Search_form(request.POST)
#        # request.session['search-query'] = request.POST
#         if form.is_valid():
#             search_query = form.cleaned_data.get('search_query')
#             search_parameter = form.cleaned_data.get('search_parameter')
#             print(search_query, search_parameter)
#             queryset_list = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
#                 company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(
#                 emails__isnull=True)[:5]
#             page = request.GET.get('page', 1)
#             paginator = Paginator(queryset_list, 2)
#
#             try:
#                 queryset = paginator.page(page)
#             except PageNotAnInteger:
#                 queryset = paginator.page(1)
#             except EmptyPage:
#                 queryset = paginator.page(paginator.num_pages)
#         return render(request,'search/search.html',{"queryset":queryset})
#     return render(request, 'search/search.html', context)

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
            print(search_query, search_parameter)
            queryset_list = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
                company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(
                emails__isnull=True)[:5]
            page = request.GET.get('page', 1)
            paginator = Paginator(queryset_list, 2)

            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                queryset = paginator.page(1)
            except EmptyPage:
                queryset = paginator.page(paginator.num_pages)

            return render(request, 'search/search_results.html', {'queryset': queryset})

    else:
        context = {
            'form': Search_form()
        }
        return render(request, 'search/search.html', context)


def show_data(search_query, search_parameter):
    queryset = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(
        company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(
        emails__isnull=True)[:5]
    return queryset

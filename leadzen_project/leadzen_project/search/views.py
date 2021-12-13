from django.shortcuts import render
from .forms import Search_form
from .models import CompanyRecords

# Create your views here.

def search(request):
    context = {
        'form': Search_form()
    }
    if request.method=='POST':
        form=Search_form(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            search_parameter=form.cleaned_data.get('search_parameter')
            print(search_query,search_parameter)
            queryset=show_data(search_query,search_parameter)
            return render(request,'search/search_results.html',{'queryset':queryset})

    return render(request, 'search/search.html', context)

def show_data(search_query,search_parameter):
    queryset = CompanyRecords.objects.filter(**{f'{search_parameter}__icontains': search_query}).exclude(company_name__isnull=True).exclude(description__isnull=True).exclude(phones__isnull=True).exclude(emails__isnull=True)[:5]
    return queryset


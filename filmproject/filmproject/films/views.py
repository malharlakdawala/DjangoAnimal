from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .models import *
from .forms import AddFilmForm,AddDirectorForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.

class FilmListView(ListView):
    model = Film
    context_object_name = 'films'
    template_name = 'homepage.html'

class FilmAddView(CreateView):
    model = Film
    form_class = AddFilmForm
    template_name = 'addFilm.html'
    success_url=reverse_lazy('homepage')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class FilmUpdateView(UpdateView):
    model=Film
    form_class = AddFilmForm
    template_name = 'addFilm.html'
    success_url=reverse_lazy('homepage')

class FilmDetailView(DetailView):
    model = Film
    form_class = AddFilmForm
    context_object_name = 'films'
    template_name = 'detailFilm.html'


def homepage(request):
    return render(request,'homepage.html')

def addFilm(request):
    pass

def addDirector(request):
    pass


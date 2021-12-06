from django.shortcuts import render
from .forms import UserRegisterForm, ProfileCreateForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import Profile, Starwars_people
import requests
import json
import time


# Create your views here.
def homepage(request):
    return render(request, 'partials/base.html')


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('homepage')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['profile_form'] = UserRegisterForm(self.request.POST or None)
    #     print(context)
    #     return context
    # used to enter a new datapoint while entering

    # def form_valid(self, form):
    #     signup_form = UserRegisterForm(self.request.POST)
    #     if signup_form.is_valid():
    #         self.object = form.save()
    #         profile = signup_form.save(commit=False)
    #         profile.user = self.object
    #         profile.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #

    # def form_invalid(self, form):
    #     # same as above
    #     print('form is invalid')
    #     return super().form_invalid(form)


class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        # this will nullify the need for a pk in the url, by default get_object is the function in
        # detail views that requires a pk or slug
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if Profile.objects.filter(user=self.request.user).exists():
            context['profile_form'] = ProfileCreateForm(self.request.POST or None, instance=self.request.user.profile)
            print(context)
            # update form
        else:
            context['profile_form'] = ProfileCreateForm(self.request.POST or None)
            print(context)
            # create form
        return context

    def form_valid(self, form):
        if Profile.objects.filter(user=self.request.user).exists():
            profile_form = ProfileCreateForm(self.request.POST, instance=self.request.user.profile)
        else:
            profile_form = ProfileCreateForm(self.request.POST)
        if profile_form.is_valid():
            self.object = form.save()
            profile = profile_form.save(commit=False)
            profile.user = self.object
            profile.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


#add Star wars data
def add_data(request):
    for i in range(30, 80):
        starwars_response = requests.get(f"https://swapi.dev/api/people/{i}/").json()
        starwars_name = starwars_response["name"]
        starwars_height = starwars_response["height"]
        if isinstance(starwars_response["mass"], int):
            starwars_mass = starwars_response["mass"]
        else:
            starwars_mass = None
        starwars_home = requests.get(starwars_response["homeworld"]).json()["name"]
        a = Starwars_people.objects.create(name=starwars_name, height=starwars_height, mass=starwars_mass,
                                           homeworld=starwars_home)
        time.sleep(2)
        print("insert sucessfull for ", i)
    return render(request, 'partials/base.html')

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'profession']

class ProfileDataForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'github', 'website', 'facebook', 'instagram', 'twitter']

class ProfileSocialForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['github', 'website', 'facebook', 'instagram', 'twitter']

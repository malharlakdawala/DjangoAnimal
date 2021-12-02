from django import forms
from .models import *
import datetime

class Add_rental(forms.Form):
    rental_date = forms.DateField(widget = forms.SelectDateWidget,initial=datetime.date.today)
    return_date = forms.DateField(required = False)
    customer=forms.ModelChoiceField(queryset=Customer.objects.all())
    vehicle=forms.ModelChoiceField(queryset=Vehicle.objects.all())

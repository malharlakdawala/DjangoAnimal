from django import forms

class Add_rental(forms.Form):
    rental_date = forms.DateField()
    field2_name = forms.TextField()

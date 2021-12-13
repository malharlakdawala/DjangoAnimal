from django import forms

class Search_form(forms.Form):
    CHOICES = (('address', 'Pincode'), ('state', 'State'),('description', 'Description'),('name', 'Name'),)
    search_parameter = forms.ChoiceField(choices=CHOICES)
    search_query = forms.CharField()

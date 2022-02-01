from django import forms


class Search_form(forms.Form):
    CHOICES = (('address', 'Pincode'), ('description', 'Description'), ('company_name', 'Name'),)
    search_parameter = forms.ChoiceField(choices=CHOICES, label='',
                                         widget=forms.Select(attrs={'class': 'search_parameter'}))
    search_query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'search_query', 'placeholder': ' Enter Address or pincode'}), label='')
    # search_parameter = forms.ChoiceField(choices=CHOICES)
    # search_query = forms.CharField()


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

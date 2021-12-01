from django import forms
from todo.models import Category,Todo
import datetime

class ContactForm(forms.Form):
      title = forms.CharField(max_length=50,label='Type Title of task',
                              help_text='This is help text')
      details = forms.CharField(error_messages={'required': 'Please enter a valid email address'})
      #date_completion = forms.DateField(initial=datetime.date.today)
      deadline_date = forms.DateField(widget = forms.SelectDateWidget,initial=datetime.date.today)
      category = forms.ModelChoiceField(queryset=Category.objects.all())

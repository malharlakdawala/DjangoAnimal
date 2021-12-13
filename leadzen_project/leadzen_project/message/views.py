import requests
import json
from django.shortcuts import render
from search.models import CompanyRecords
from django.http import HttpResponse

# Create your views here.
def message(request,str):
    queryset=CompanyRecords.objects.get(uuid_field=str)
    email = queryset.emails.split(",")
    phone = queryset.phones.split(",")
    contact_person=''.join(queryset.contact_person.split())
    return render(request, "message.html", {"queryset":queryset, "email": email, "phone":phone, "contact_person":contact_person})

def email(request,str):
    pass

def call(request,str):
    pass

def sms(request,str):
    pass

def whatsapp(request,phn,name):
    url = 'https://api.tellephant.com/v1/send-message'
    payload = {
        "apikey": "4v8dob0yjfTewtxe1NkaS0sHWeXgwluzmbD9HF8jAn8pD21ZKSsRhzaZ8AZTeKxqWKaqONtdVAq",
        "to": phn,
        "channels": [
            "whatsapp"
        ],
        "whatsapp": {
            "contentType": "template",
            "template": {
                "templateId": "a_great_news",
                "language": "en",
                "components": [{"type": "body", "parameters": [{"type": "text", "text": name}]}]
            }
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request('POST', url, headers=headers, json=payload)
    print(response.json().values)
    return HttpResponse(str("Whatsapp message sent succesfully"))






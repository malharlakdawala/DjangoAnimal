import requests
import json
from django.shortcuts import render
from search.models import CompanyRecords
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from search.forms import Search_form


# Create your views here.
def message(request,str):
    queryset=CompanyRecords.objects.get(uuid_field=str)
    email = queryset.emails.split(",")
    phone = queryset.phones.split(",")
    contact_person=''.join(queryset.contact_person.split())
    form=Search_form()
    return render(request, "message.html", {"queryset":queryset, "email": email, "phone":phone, "contact_person":contact_person,'form':form})

def email(request,mails):
    mail_list = list(mails.split(","))
    send_mail(
        subject="Test Email",
        message="Hello how are you. This is a test email",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=mail_list)
    return HttpResponse(status=204)


def call(request,phn,name):
    phn=str(phn)
    phone_no = phn[:2]+"0"+phn[2:]
    print(phone_no)
    url = "https://product.hr.frejun.com/api/v1/integrations/create-call/"

    parameters = {
        "recruiter_email": "zeel.mehta@kapso.in",
        "transaction_id": "1",
        "job_id": "SDE",
        "candidate_id": "1",
        "candidate_number": phone_no,
        "candidate_name": name
    }

    r = requests.post(url, headers={'Authorization': 'Api-Key zRyfu7IZ.Ni1nkhbLhj2TfYgF0cn33d8ekltz6lE0'},data=parameters)

    print(r.text)
    return HttpResponse(status=204)


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
    return HttpResponse(status=204)







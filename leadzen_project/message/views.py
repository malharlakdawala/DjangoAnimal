import time

import requests
import json
from django.shortcuts import render
from search.models import CompanyRecords
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from search.forms import Search_form
from .cleanfile import Cleanstring

message_id = []


# Create your views here.
def message(request, str):
    queryset = CompanyRecords.objects.get(uuid_field=str)
    contact_person = ''.join(queryset.contact_person.split()) if (
            queryset.contact_person and queryset.contact_person != '') else "hi"
    phone = queryset.phones.split(",") if (queryset.phones and queryset.phones != '') else [1]
    email = queryset.emails.split(",") if (queryset.emails and queryset.emails != '') else [
        "levelupmultilink@gmail.com"]
    form = Search_form()
    a = Cleanstring()
    ai_description = a.clean(queryset.description)
    return render(request, "message.html",
                  {"queryset": queryset, "email": email, "phone": phone, "contact_person": contact_person,
                   'form': form, "ai_description": ai_description})


def email(request, mails):
    mail_list = list(mails.split(","))
    msg = request.GET.get('chat_text_input')

    send_mail(
        subject="Test Email",
        message="Test mail",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=mail_list)
    return HttpResponse(status=204)


def call(request, phn, name):
    phn = str(phn)
    phone_no = phn[:2] + "0" + phn[2:]
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

    r = requests.post(url, headers={'Authorization': 'Api-Key zRyfu7IZ.Ni1nkhbLhj2TfYgF0cn33d8ekltz6lE0'},
                      data=parameters)

    print(r.text)
    return HttpResponse(status=204)


def sms(request, phn):
    URL = "http://2factor.in/API/V1/3adf9525-efb4-11eb-8089-0200cd936042/ADDON_SERVICES/SEND/TSMS"
    data = {'From': "ERSSTD", 'To': phn, "TemplateName": "OTPVerification3", "Var1": "ee"}
    r = requests.post(url=URL, data=data)
    print(r)
    return HttpResponse(status=204)


def whatsapp(request, phn, name):
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
    print(response.text)
    msg_id = response.text

    url_whatsapp_log = "https://api.tellephant.com/v1/message-history"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = "{\"apikey\" : \"4v8dob0yjfTewtxe1NkaS0sHWeXgwluzmbD9HF8jAn8pD21ZKSsRhzaZ8AZTeKxqWKaqONtdVAq\",    \"messageId\" : \"msg_id\"}"
    time.sleep(5)
    response_log = requests.request("POST", url, headers=headers, data=payload)
    print(response_log.text)
    message_id.append(response_log.text)
    return HttpResponse(status=204)


def logs(request, id):
    form = Search_form()
    response = requests.get("https://product.hr.frejun.com/api/v1/integrations/calls/?page_size=8",
                            headers={'Authorization': 'Api-Key zRyfu7IZ.Ni1nkhbLhj2TfYgF0cn33d8ekltz6lE0'})
    response = response.json()
    print(response["results"])
    switch = {'recruiter-not-available': 'Not Available', 'answered': 'Answered', 'rec-busy/not_available': 'Busy',
              'not_available': "Not Available", 'ongoing..':"Answered"}
    for arr in response["results"]:
        call_status = arr["status"]
        if call_status in switch:
            arr["status"] = (switch[call_status])

    return render(request, 'logs.html', {"response": response, 'form': form})


def whatsapp_log(request, id):
    form = Search_form()
    print(message_id)
    msg_response = message_id
    return render(request, 'whatsapp_log.html', {"msg_response": msg_response, 'form': form})

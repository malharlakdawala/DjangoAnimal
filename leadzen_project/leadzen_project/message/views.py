import requests
import json
from django.shortcuts import render
from search.models import CompanyRecords
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from search.forms import Search_form

message_id=[]
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
    print(response.text)
    message_id.append(response.text)
    return HttpResponse(status=204)

def logs(request,id):
    form = Search_form()
    response=requests.get("https://product.hr.frejun.com/api/v1/integrations/calls/?page_size=8",headers={'Authorization': 'Api-Key zRyfu7IZ.Ni1nkhbLhj2TfYgF0cn33d8ekltz6lE0'})
    a=response.json()
    print("count",a["count"])
    print(a["results"][0]["candidate_name"])

    return render(request,'logs.html',{"response":a,'form':form})

def whatsapp_log(request,id):
    form = Search_form()
    url = "https://api.tellephant.com/v1/message-history"
    headers = {
        'Content-Type': 'application/json'
    }
    msg_response=[]
    for msg_id in message_id:
        payload= "{\"apikey\" : \"4v8dob0yjfTewtxe1NkaS0sHWeXgwluzmbD9HF8jAn8pD21ZKSsRhzaZ8AZTeKxqWKaqONtdVAq\",    \"messageId\" : \"61bf4284d0635326bd2623d7\"}"
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        msg_response.append(response.text)
    return render(request, 'whatsapp_log.html', {"msg_response": msg_response, 'form': form})




# telephant
import requests
import json

url = 'https://api.tellephant.com/v1/send-message'
payload = {
    "apikey": "4v8dob0yjfTewtxe1NkaS0sHWeXgwluzmbD9HF8jAn8pD21ZKSsRhzaZ8AZTeKxqWKaqONtdVAq",
    "to": 919769494336,
    "channels": [
        "whatsapp"
    ],
    "whatsapp": {
        "contentType": "template",
        "template": {
            "templateId": "a_great_news",
            "language": "en",
            "components": [{"type": "body", "parameters": [{"type": "text", "text": "Malhar"}]}]
        }
    }
}
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
response = requests.request('POST', url, headers=headers, json=payload)
print(response.json())

# frejun


cLk68mvg.g1ug5GBcTcWRfkvhMtAypc3jnEZmPm6r

# url = 'https://api.tellephant.com/v1/send-message'
# payload = {
#     "apikey": "g1ug5GBcTcWRfkvhMtAypc3jnEZmPm6r",
#     "to": 919769494336,
#     "channels": [
#         "whatsapp"
#     ],
#     "whatsapp": {
#         "contentType": "template",
#         "template": {
#             "templateId": "dummy_template_name",
#             "language": "en",
#             "components": []
#         }
#     }
# }
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': 'application/json'
# }
# response = requests.request('POST', url, headers=headers, json=payload)
# print(response.json())


# <iframe width="600" height="450" style="border:0" loading="lazy" allowfullscreen src="https://www.google.com/maps/embed/v1/place?q=challenger%20towers%20kandivali%20east&key=AIzaSyCWpr1t7055e-ZTjV-NHWNI3SQmV8f792w"></iframe>

#from .models import Starwars_people
#import .models
import requests
import json
import time

# for i in range(1, 3):
#     starwars_response = requests.get(f"https://swapi.dev/api/people/{i}/").json()
#     starwars_name = starwars_response["name"]
#     starwars_height = starwars_response["height"]
#     starwars_mass = starwars_response["mass"]
#     starwars_home = requests.get(starwars_response["homeworld"]).json()["name"]
#     a = Starwars_people.objects.create(name=starwars_name, height=starwars_height, mass=starwars_mass,
#                                        homeworld=starwars_home)
#     time.sleep(2)
#     print("insert sucessfull for ", i)

from django.shortcuts import render
import requests
import json
import time
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Deck, Transaction
from accounts.models import Starwars_people
from django.contrib.auth.models import User


def my_cards(request):
    if request.user.is_authenticated:
        get_deck_object_user=Deck.objects.filter(profile=request.user).values()
        object_id=get_deck_object_user[0]["id"]
        cards_list=Starwars_people.objects.filter(deck=object_id)
        #print(cards_list)
        return render(request, 'my_cards.html',{'cards_list':cards_list})

def transfer(request,id):
    cards_sender_id=request.user.id
    card_details_id=id
    print(cards_sender_id,card_details_id)
    Transaction.objects.create(cards_sender_id=cards_sender_id,card_details_id=card_details_id)
    return render(request, 'homepage.html')

def homepage(request):
    transaction_live = []
    queryset=Transaction.objects.all()
    for transaction in queryset:
        username = User.objects.get(id=transaction.id).username
        card_name = Starwars_people.objects.get(id=transaction.card_details_id).name
        card_height = Starwars_people.objects.get(id=transaction.card_details_id).height
        card_mass = Starwars_people.objects.get(id=transaction.card_details_id).mass
        card_homeworld = Starwars_people.objects.get(id=transaction.card_details_id).homeworld
        date_created=transaction.date_created
        transaction_status=transaction.transaction_status
        transaction_id=transaction.id
        dict={
            'username':username,
            'card_name':card_name,
            'card_height':card_height,
            'card_mass':card_mass,
            'card_homeworld':card_homeworld,
            'date_created':date_created,
            'transaction_status':transaction_status,
            'transaction_id':transaction_id
              }
        transaction_live.append(dict)
    return render(request, 'homepage.html',{'transaction_live':transaction_live})


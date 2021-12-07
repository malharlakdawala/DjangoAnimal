from django import forms
from .models import Deck,Transaction
from accounts.models import Starwars_people


class SelectCard(forms.Form):
    your_cards = forms.ModelChoiceField(queryset=Starwars_people.objects.none())

    def __init__(self,user,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["your_cards"].queryset=user.profile.deck.cards.all()
        #this user's cards


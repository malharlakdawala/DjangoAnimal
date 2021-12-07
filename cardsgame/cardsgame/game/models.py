from django.db import models
from django.contrib.auth.models import User
from accounts.models import Starwars_people

# Create your models here.
#Card module already defined in accounts/models as Starwars_people

class Deck(models.Model):
    profile=models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Starwars_people)

    # def __str__(self):
    #     return self.cards

class Transaction(models.Model):
    cards_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards_sender')
    cards_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards_receiver',null=True)
    card_details = models.ForeignKey(Starwars_people, on_delete=models.CASCADE, related_name='cards_details')
    transaction_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    card_received = models.ForeignKey(Starwars_people, on_delete=models.CASCADE, related_name='cards_received',null=True)

#fk to key
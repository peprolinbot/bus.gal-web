from django.db import models

from .utils.account import account

class Owner(models.Model):
    email = models.CharField(unique=True, max_length=254)

    def __str__(self):
        return f"{self.email}"


class Card(models.Model):
    def update_pending(self):
        self.last_pending = account.get_card(self.number).pending
        self.save()

        return self.last_pending

    number = models.IntegerField(unique=True, null=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    last_pending = models.FloatField(default=0)

    def __str__(self):
        return f"{self.owner.email}'s {self.number}"

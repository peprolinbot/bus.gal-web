from django import forms

from .models import Card


class CardNumberForm(forms.Form):
    card_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': '0000 0000 0000 0000'}))


class AddCardForm(CardNumberForm):
    email = forms.CharField(max_length=254)

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from .forms import AddCardForm, CardNumberForm
from .models import Card, Owner
from .utils.account import account

from busGal_api.exceptions import TPGalWSAppException

def index(request):
    return render(request, 'xenovaping/index.html')

def add_card(request):
    if request.method == 'POST':
        form = AddCardForm(request.POST)

        if form.is_valid():
            card_number = form.cleaned_data["card_number"]
            try:
                account.add_card(card_number, card_number)
            except TPGalWSAppException as e:
                message = e.app_error.message
                form.add_error('card_number', message)
            else:
                email = form.cleaned_data["email"]
                owner, created = Owner.objects.get_or_create(email=email)

                card = Card.objects.create(number=card_number, owner=owner)
                pending = card.update_pending()
                messages.success(
                    request, f"Card added succesfully, you have {pending}€ pending of refund. Next time this number grows, you'll be e-mailed 💌")

    else:
        form = AddCardForm()

    return render(request, 'xenovaping/add_card.html', {'form': form})


def remove_card(request):
    if request.method == 'POST':
        form = CardNumberForm(request.POST)

        if form.is_valid():
            card_number = form.cleaned_data["card_number"]
            try:
                account.delete_card(card_number)
            except TPGalWSAppException as e:
                message = e.app_error.message
                form.add_error('card_number', message)
            else:
                card = Card.objects.get(number=card_number)
                card.delete()
                messages.success(
                    request, f"Card removed succesfully, have a nice day 😘")

    else:
        form = CardNumberForm(request.GET) if request.GET else CardNumberForm()

    return render(request, 'xenovaping/remove_card.html', {'form': form})

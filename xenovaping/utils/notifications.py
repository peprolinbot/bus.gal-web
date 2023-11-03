from ..models import Card
from .account import account

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

from busGal_api.exceptions import TPGalWSAppException


def notify_email(email, number, pending):
    html_body = render_to_string("xenovaping/email/cashback_notification.html", {
                                 'base_url': settings.EMAIL_BASE_URL, 'pending': pending, 'number': number})

    send_mail(subject="Refund avaliable",
              message=f"Hi there, you have a pending cashback of {pending}€ on your Xente Nova card with number {number}. You can go to your nearest ABANCA ATM to claim them.\nThis project is not endorsed by, directly affiliated with, maintained by, sponsored by or in any way officially related with la Xunta de Galicia, the bus operators or any of the companies involved in the bus.gal website and/or the app.",
              from_email=None,
              recipient_list=[email],
              fail_silently=True,
              html_message=html_body)


def run_checks():
    # This logic may seem wird, but its objective is to just call the api once, as it's slow AF
    try:
        cards_summary = account.get_cards()
    except TPGalWSAppException as e:
        if e.app_error.code == '087':  # 087: User has no cards
            return
        raise e
    for api_card in cards_summary:
        db_card = Card.objects.get(number=api_card.number)

        if api_card.pending > db_card.last_pending:
            notify_email(db_card.owner.email, db_card.number, api_card.pending)

        db_card.last_pending = api_card.pending
        db_card.save()

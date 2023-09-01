from django.conf import settings

from busGal_api.accounts import Account

account = Account(email=settings.TPGAL_USER, password=settings.TPGAL_PASSWORD)
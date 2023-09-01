from django.conf import settings

from busGal_api.accounts import Account

if settings.IS_DOCKER_BUILD:
    account = None
else:
    account = Account(email=settings.TPGAL_USER, password=settings.TPGAL_PASSWORD)

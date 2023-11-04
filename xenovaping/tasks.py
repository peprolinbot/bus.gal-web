from django.conf import settings

import sys

from django_q.models import Schedule


def setup_tasks():
    if not settings.IS_DOCKER_BUILD and not 'migrate' in sys.argv:
        Schedule.objects.get_or_create(name="Check and send the neccesary 'pending refund' notifications",
                                       func='xenovaping.utils.notifications.run_checks',
                                       schedule_type=Schedule.DAILY)

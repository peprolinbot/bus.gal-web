from django.conf import settings

from django_q.models import Schedule


def setup_tasks():
    if not settings.IS_DOCKER_BUILD:
        Schedule.objects.get_or_create(name="Check and send the neccesary 'pending refund' notifications",
                                       func='xenovaping.utils.notifications.run_checks',
                                       schedule_type=Schedule.DAILY)

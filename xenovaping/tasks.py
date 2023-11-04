from django_q.models import Schedule


def setup_tasks():
    Schedule.objects.get_or_create(name="Check and send the neccesary 'pending refund' notifications",
                                   func='xenovaping.utils.notifications.run_checks',
                                   schedule_type=Schedule.DAILY)

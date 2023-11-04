from django_q.models import Schedule


def setup_tasks():
    Schedule.objects.get_or_create(name="Update the bus stops search index",
                                   func='buses.utils.stops_cache.stops_cache.update_index',
                                   schedule_type=Schedule.MINUTES,
                                   minutes=2)

from django.utils.timezone import localtime


def get_duration(start, end):
    return (end - localtime(start)).total_seconds()


def format_duration(duration):
    seconds = 60
    hour = seconds**2
    hours = int(duration // hour)
    minutes = int((duration - hours * seconds**2) // seconds)
    return f'{hours:02d}:{minutes:02d}'


def is_visit_long(start, end, minutes=60):
    time_if_guard = 23*minutes**2 + 58*minutes
    return time_if_guard > get_duration(start, end) > minutes*60


def is_strange(visits):
    return any(
        is_visit_long(visit.entered_at, visit.leaved_at)
        for visit in visits
    )

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit

from datacenter.duration_and_check import format_duration
from datacenter.duration_and_check import get_duration
from datacenter.duration_and_check import is_strange


def storage_information_view(request):
    non_closed_visits = []
    non_leaved_persons = Visit.objects.filter(leaved_at__isnull=True)
    for person in non_leaved_persons:
        visits = Visit.objects.filter(
            passcard=person.passcard,
            leaved_at__isnull=False
        )
        non_closed_visits.append(
            {
                'who_entered': person.passcard.owner_name,
                'entered_at': person.entered_at,
                'duration': format_duration(get_duration(
                                person.entered_at,
                                localtime())
                ),
                'is_strange': is_strange(visits)
            },
        )
    context = {
        'non_closed_visits': non_closed_visits,
        }
    return render(request, 'storage_information.html', context)

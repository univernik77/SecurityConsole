from django.shortcuts import get_object_or_404
from django.shortcuts import render

from datacenter.models import Visit
from datacenter.models import Passcard
from datacenter.duration_and_check import format_duration
from datacenter.duration_and_check import get_duration
from datacenter.duration_and_check import is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard, leaved_at__isnull=False)
    for visit in visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(
                    get_duration(visit.entered_at, visit.leaved_at)
                ),
                'is_strange': is_visit_long(visit.entered_at, visit.leaved_at)
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

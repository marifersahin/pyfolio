# Create your views here.
from django.http import Http404
from django.shortcuts import render_to_response
from entry.models import Entry


def entry_list(request):
    entries = Entry.objects.all()
    return render_to_response('entry/entry_list.html', {'entries': entries})


def entry_detail(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Poll.DoesNotExist:
        raise Http404("Entry does not exist")
    return render_to_response('entry/entry_detail.html', {'entry': entry})


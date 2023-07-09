from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .forms import SearchForm

import busGal_api as busapi
from datetime import datetime
import time
import json


def index(request):
    form = SearchForm(initial=request.GET)
    return render(request, 'buses/index.html', {'form': form})


def autocomplete(request):
    query = request.GET.get("text")
    stops = busapi.search_stop(query)[:2]

    options = [{"value": stop.id, "text": stop.name} for stop in stops]

    return JsonResponse({"options": options})


def search(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        origin_id = int(form.cleaned_data['origin'])
        destination_id = int(form.cleaned_data['destination'])
        timestamp = int(time.mktime(form.cleaned_data['date'].timetuple()))

    return HttpResponseRedirect(reverse('buses:results', args=(origin_id, destination_id, timestamp)))


def results(request, origin_id, destination_id, timestamp):  # Date is a UNIX timestamp
    stops = busapi.get_stops()
    stop_ids = [stop.id for stop in stops]
    origin = stops[stop_ids.index(origin_id)]
    destination = stops[stop_ids.index(destination_id)]

    date = datetime.fromtimestamp(timestamp)

    trip = busapi.Trip(origin, destination, date)

    return render(request, 'buses/results.html', {'origin': trip.origin, 'destination': trip.destination, 'date': trip.date, 'timestamp': timestamp, 'expeditions': trip.expeditions})

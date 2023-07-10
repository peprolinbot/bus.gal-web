from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import SearchForm

import busGal_api as busapi
from datetime import datetime
import time


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        # To make the form valid
        origin_id = request.POST.get("origin")
        destination_id = request.POST.get("destination")
        form.fields['origin'].choices = [(origin_id, origin_id)]
        form.fields['destination'].choices = [(destination_id, destination_id)]

        if form.is_valid():
            origin_id = int(form.cleaned_data['origin'])
            destination_id = int(form.cleaned_data['destination'])
            timestamp = int(time.mktime(form.cleaned_data['date'].timetuple()))

            return redirect('buses:results', origin_id, destination_id, timestamp)
    else:
        form = SearchForm(initial=request.GET)

    return render(request, 'buses/index.html', {'form': form})


def autocomplete(request):
    query = request.GET.get("q")
    stops = busapi.search_stop(query)

    options = [{"id": stop.id, "text": stop.name} for stop in stops]

    return JsonResponse({"results": options})


def results(request, origin_id, destination_id, timestamp):  # Date is a UNIX timestamp
    stops = busapi.get_stops()
    stop_ids = [stop.id for stop in stops]
    origin = stops[stop_ids.index(origin_id)]
    destination = stops[stop_ids.index(destination_id)]

    date = datetime.fromtimestamp(timestamp)

    trip = busapi.Trip(origin, destination, date)

    return render(request, 'buses/results.html', {'origin': trip.origin, 'destination': trip.destination, 'date': trip.date, 'timestamp': timestamp, 'expeditions': trip.expeditions})

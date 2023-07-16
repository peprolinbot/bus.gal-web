from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import SearchForm
from .templatetags.buses_extras import form_stop_string as _create_form_stop_string

from busGal_api import transport as busapi
from datetime import date
import time


def _parse_form_stop_string(string: str) -> busapi.stops.Stop:
    return busapi.stops.Stop(*string.split("/", 2))


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        # To make the form valid
        origin_id = request.POST.get("origin")
        destination_id = request.POST.get("destination")
        form.fields['origin'].choices = [(origin_id, origin_id)]
        form.fields['destination'].choices = [(destination_id, destination_id)]

        if form.is_valid():
            origin = _parse_form_stop_string(form.cleaned_data['origin'])
            destination = _parse_form_stop_string(
                form.cleaned_data['destination'])

            timestamp = int(time.mktime(form.cleaned_data['date'].timetuple()))

            return redirect('buses:results', origin.id, origin.type, origin.name, destination.id, destination.type, destination.name, timestamp)
    else:
        form = SearchForm()

        origin = request.GET.get("origin")  # form_stop_string
        destination = request.GET.get("destination")  # form_stop_string
        if origin:
            form.fields['origin'].choices = [
                (origin, _parse_form_stop_string(origin).name)]
            form.fields['origin'].initial = origin
        if destination:
            form.fields['destination'].choices = [
                (destination, _parse_form_stop_string(destination).name)]
            form.fields['destination'].initial = destination

    return render(request, 'buses/index.html', {'form': form})


def autocomplete(request):
    query = request.GET.get("q")
    stops = busapi.stops.search_stops(query)

    options = [{"id": _create_form_stop_string(stop), "text": stop.name}
               for stop in stops]

    return JsonResponse({"results": options})


def results(request, origin_id, origin_type, origin_name, destination_id, destination_type, destination_name, timestamp):  # Date is a UNIX timestamp
    origin = busapi.stops.Stop(
        id=origin_id,
        type=origin_type,
        name=origin_name)
    destination = busapi.stops.Stop(
        id=destination_id,
        type=destination_type,
        name=destination_name)

    trip_date = date.fromtimestamp(timestamp)

    expeditions = busapi.expeditions.search_expeditions(
        origin, destination, trip_date)

    return render(request, 'buses/results.html', {'origin': origin,
                                                  'destination': destination,
                                                  'date': trip_date,
                                                  'timestamp': timestamp,
                                                  'expeditions': expeditions})

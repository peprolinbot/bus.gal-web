from django import forms

import busGal_api as busapi
import datetime


class SearchForm(forms.Form):
    def get_choice_stops():
        stops = busapi.get_stops()
        choices = [(stop.id, stop.name) for stop in stops]
        return choices
    choices = get_choice_stops()
    origin = forms.ChoiceField(label='Origin', choices=choices, widget=forms.Select(
        attrs={'class': 'selectpicker form-control', 'data-live-search': 'true'}))
    destination = forms.ChoiceField(label='Destination', choices=choices, widget=forms.Select(
        attrs={'class': 'selectpicker form-control', 'data-live-search': 'true'}))

    def get_current_date_formatted():
        return datetime.date.today().strftime("%Y-%m-%d")
    date = forms.DateField(label='Date', initial=datetime.date.today, widget=forms.DateInput(attrs={
                           'type': 'date', 'min': get_current_date_formatted}))  # type=date for the bootstrap+system datepicker to appear

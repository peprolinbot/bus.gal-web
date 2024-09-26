from django import forms

import busGal_api as busapi
import datetime


class StopSearchForm(forms.Form):
    stop = forms.ChoiceField(required=True, label='Stop', widget=forms.Select(
        attrs={'class': 'select2', 'data-placeholder': 'Start typing to search'}))


class TripSearchForm(forms.Form):
    origin = forms.ChoiceField(required=True, label='Origin', widget=forms.Select(
        attrs={'class': 'select2', 'data-placeholder': 'Start typing to search'}))

    destination = forms.ChoiceField(required=True, label='Destination', widget=forms.Select(
        attrs={'class': 'select2', 'data-placeholder': 'Start typing to search'}))

    def get_current_date_formatted():
        return datetime.date.today().strftime("%Y-%m-%d")

    date = forms.DateField(required=True, label='Date', initial=datetime.date.today, widget=forms.DateInput(attrs={
                           'class': 'bg-white text-black', 'type': 'date', 'min': get_current_date_formatted}))  # type=date for the bootstrap+system datepicker to appear

from django import forms

import busGal_api as busapi
import datetime


class SearchForm(forms.Form):
    origin = forms.ChoiceField(label='Origin', widget=forms.Select(
        attrs={'class': 'selectpicker form-control', 'data-live-search': 'true', 'data-style': 'btn-success'}))

    destination = forms.ChoiceField(label='Destination', widget=forms.Select(
        attrs={'class': 'selectpicker form-control', 'data-live-search': 'true', 'data-style': 'btn-warning'}))

    def get_current_date_formatted():
        return datetime.date.today().strftime("%Y-%m-%d")

    date = forms.DateField(label='Date', initial=datetime.date.today, widget=forms.DateInput(attrs={
                           'type': 'date', 'min': get_current_date_formatted}))  # type=date for the bootstrap+system datepicker to appear

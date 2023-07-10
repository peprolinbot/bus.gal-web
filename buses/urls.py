from django.urls import path

from . import views

app_name = 'buses'
urlpatterns = [
    path('', views.index, name='index'),
    path('autocomplete', views.autocomplete, name='autocomplete'),
    path('results/<int:origin_id>/<int:destination_id>/<int:timestamp>',
         views.results, name='results'),  # Date is a UNIX timestamp
]

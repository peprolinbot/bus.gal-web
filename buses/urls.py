from django.urls import path

from . import views

app_name = 'buses'
urlpatterns = [
    path('', views.index, name='index'),
    path('autocomplete', views.autocomplete, name='autocomplete'),
    path('results/<int:origin_id>/<str:origin_type>/<str:origin_name>/<int:destination_id>/<str:destination_type>/<str:destination_name>/<int:timestamp>',
         views.results, name='results'),  # Date is a UNIX timestamp
    path('results/<int:origin_id>/<str:origin_type>/<str:origin_name>/<int:destination_id>/<str:destination_type>/<str:destination_name>',
         views.results, name='results'),  # Without date (is optional)
]

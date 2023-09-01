from django.urls import path

from . import views

app_name = 'xenovaping'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_card', views.add_card, name='add_card'),
    path('remove_card', views.remove_card, name='remove_card')
]

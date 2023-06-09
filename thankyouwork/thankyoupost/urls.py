from django.urls import path
from .views import thankyoupost_list

app_name = 'thankyoupost'

urlpatterns = [
    path('', thankyoupost_list, name='thankyoupost_list'),
]

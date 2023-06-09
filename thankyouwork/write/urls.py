from django.urls import path
from .views import write_post

app_name = 'write'

urlpatterns = [
    path('', write_post, name='write_post'),

]

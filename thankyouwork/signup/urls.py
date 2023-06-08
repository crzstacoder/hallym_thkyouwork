from django.urls import path
from .views import SignUpView

appname = 'signup'

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
]

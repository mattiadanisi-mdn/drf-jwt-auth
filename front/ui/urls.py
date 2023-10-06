from django.urls import path

from .views import RegistrationView

app_name = 'ui'
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration')
]

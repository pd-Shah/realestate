from django.urls import path
from .views import (
    SendSMS,
    CheckCode,
)


app_name = "sms"
urlpatterns = [
    path(
        '',
        SendSMS.as_view(),
        name='loging_sms'
    ),
    path(
        'check-code',
        CheckCode.as_view(),
        name='check_code'
    ),
]

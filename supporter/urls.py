from django.urls import path
from .views import (
    RegisterSupporterView,
)

app_name = "supporter"

urlpatterns = [
    path(
        '',
        RegisterSupporterView.as_view(),
        name='register_supporter'
    ),
]

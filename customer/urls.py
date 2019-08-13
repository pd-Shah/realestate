from django.urls import path
from .views import (
    remove_phone_ad_view,
    set_phone_ad_view,
)

app_name = "customer"

urlpatterns = [
    path("set/<int:pk>", set_phone_ad_view, name="set_phone_ad"),
    path("remove/<int:pk>", remove_phone_ad_view, name="remove_phone_ad"),
]

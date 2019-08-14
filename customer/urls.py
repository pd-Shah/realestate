from django.urls import path
from .views import (
    set_fav_view,
    set_unfav_view,
)

app_name = "customer"

urlpatterns = [
    path(
        'fav/<int:advertisement_id>/',
        set_fav_view,
        name='set_favourite'
    ),
    path(
        'unfav/<int:advertisement_id>/',
        set_unfav_view,
        name='set_unfavourite'
    ),
]

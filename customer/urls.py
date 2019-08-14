from django.urls import path
from .views import (
    set_fav_view,
    set_unfav_view,
)

app_name = "customer"

urlpatterns = [
    path(
        'fav/',
        set_fav_view,
        name='set_favourite'
    ),
    path(
        'unfav/',
        set_unfav_view,
        name='set_unfavourite'
    ),
]

from django.urls import path
from .views import (
    AdvertisementListView,
)

urlpatterns = [
    path('', AdvertisementListView.as_view(), name="index")
]

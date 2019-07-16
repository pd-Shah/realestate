from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementListViewMap,
    AboutUsView,
)

app_name = 'advertisement'
urlpatterns = [
    path('', AdvertisementListView.as_view(), name="advertisement_list"),
    path('map/', AdvertisementListViewMap.as_view(), name="advertisement_list_map"),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
]

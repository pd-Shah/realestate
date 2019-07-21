from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementListViewMap,
    AboutUsView,
    SelectAddView,
    NewRentApartment,
)

app_name = 'advertisement'
urlpatterns = [
    path('', AdvertisementListView.as_view(), name="advertisement_list"),
    path('map/', AdvertisementListViewMap.as_view(), name="advertisement_list_map"),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('select/', SelectAddView.as_view(), name='select_ad'),
    path('new-apartment-rent/', NewRentApartment.as_view(), name='new-partment-rent'),
]

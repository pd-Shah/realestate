from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementListViewMap,
    AboutUsView,
    AddAddView,
)

app_name = 'advertisement'
urlpatterns = [
    path('', AdvertisementListView.as_view(), name="advertisement_list"),
    path('map/', AdvertisementListViewMap.as_view(), name="advertisement_list_map"),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('register-add/', AddAddView.as_view(), name='add_ad'),
]

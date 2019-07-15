from django.urls import path
from .views import (
    AdvertisementListView,
    AboutUsView,
)

app_name = 'advertisement'
urlpatterns = [
    path('', AdvertisementListView.as_view(), name="index"),
    path('about-us/', AboutUsView.as_view(), name='about_us')
]

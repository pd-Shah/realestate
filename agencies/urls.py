from django.urls import path
from .views import (
    AgenciesListView,
    AgenciesDetailView,
    signup,
    AgenciesLoginView,
    AgenciesAdsView,
    AgenciesSimillarAdsView,
    AgenciesMarkedAdsView,
)

app_name = "agencies"

urlpatterns = [
    path(
        'agencies-list/',
        AgenciesListView.as_view(),
        name='agencies_list'
    ),
    path(
        'agencies-list/<int:pk>/',
        AgenciesDetailView.as_view(),
        name='agencies_detail',
    ),
    path('signup/', signup, name='signup', ),
    path('login/', AgenciesLoginView.as_view(), name='login'),
    path('my-ads/', AgenciesAdsView.as_view(), name="my_ads"),
    path('simillar-ads/', AgenciesSimillarAdsView.as_view(), name="simillar_ads"),
    path('marked-ads/', AgenciesMarkedAdsView.as_view(), name="marked_ads"),
]

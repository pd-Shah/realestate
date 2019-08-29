from django.urls import path
from .views import (
    ConsultantListView,
    ConsultantDetailView,
    signup,
    ConsultantLoginView,
    ConsultantAdsView,
    ConsultantSimillarAdsView,
    ConsultantMarkedAdsView,
    LogingSingup,
)

app_name = "consultant"

urlpatterns = [
    path(
        'consultant-list/',
        ConsultantListView.as_view(),
        name='consultant_list'
    ),
    path(
        'consultant-list/<int:pk>/',
        ConsultantDetailView.as_view(),
        name='consultant_detail',
    ),
    path('signup/', signup, name='signup', ),
    path('login/', ConsultantLoginView.as_view(), name='login'),
    path('my-ads/', ConsultantAdsView.as_view(), name="my_ads"),
    path('simillar-ads/', ConsultantSimillarAdsView.as_view(), name="simillar_ads"),
    path('marked-ads/', ConsultantMarkedAdsView.as_view(), name="marked_ads"),
    path('login-singup/', LogingSingup.as_view(), name="login_or_signup"),
]

from django.urls import path
from .views import (
    ConsultantListView,
    ConsultantDetailView,
)

app_name = "consultant"

urlpatterns = [
    path(
        'consultant-list/',
        ConsultantListView.as_view(),
        name='consultant_list'
    ),
    path(
        'updateme/',
        ConsultantDetailView.as_view(),
        name='consultant_detail',
    ),

]

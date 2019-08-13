from django.urls import path
from .views import (
    ConsultantListView,
    ConsultantDetailView,
    signup,
    ConsultantLoginView,
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

]

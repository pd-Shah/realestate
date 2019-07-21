from django.views.generic import (
    ListView,
    TemplateView,
)
from . models import Advertisement
# Create your views here.


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'


class AdvertisementListViewMap(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list_map.html'


class AboutUsView(TemplateView):
    template_name = 'advertisement/about_us.html'


class AddAddView(TemplateView):
    template_name = 'advertisement/register_new_ad.html'

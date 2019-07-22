from django.views.generic import (
    ListView,
    TemplateView,
    FormView,
)
from django.urls import reverse_lazy
from . models import Advertisement
from . forms import RentApartment
# Create your views here.


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'


class AdvertisementListViewMap(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list_map.html'


class AboutUsView(TemplateView):
    template_name = 'advertisement/about_us.html'


class SelectAddView(TemplateView):
    template_name = 'advertisement/select.html'


class NewRentApartment(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentApartment
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)

    # def pre_save(self, obj):
    #


# class NewSellApartment(FormView):
#     template_name =

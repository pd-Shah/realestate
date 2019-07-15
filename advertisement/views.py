from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)
from . models import Advertisement
# Create your views here.


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'


class AboutUsView(TemplateView):
    template_name = 'advertisement/about_us.html'

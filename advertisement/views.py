from django.views.generic import (
    ListView,
    TemplateView,
    FormView,
    DetailView,
)
from django.urls import reverse_lazy
from . models import Advertisement
from . forms import (
    RentApartment,
    SellBuyApartment,
    RentEdari,
    SellBuyEdari,
    RentColangi,
    SellBuyColangi,
    RentSuit,
    SellBuySuit,
    RentVila,
    SellBuyVila,
    RentTejari,
    SellBuyTejari,
    RentZamin,
    SellBuyZamin,
    RentBagh,
    SellBuyBagh,
    RentAnbar,
    SellBuyAnbar,
    RentSole,
    SellBuySole,
)


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement/advertisment_detail.html'


class AdvertisementListViewMap(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list_map.html'


class AboutUsView(TemplateView):
    template_name = 'advertisement/about_us.html'


class SelectAddView(TemplateView):
    template_name = 'advertisement/select.html'


class NewBuyApartment(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyApartment
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'0'
        form.save()
        return super().form_valid(form)


class NewSellApartment(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyApartment
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'1'
        form.save()
        return super().form_valid(form)


class NewRentApartment(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentApartment
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'2'
        form.save()
        return super().form_valid(form)


class NewBuyEdari(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyEdari
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'3'
        form.save()
        return super().form_valid(form)


class NewSellEdari(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyEdari
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'4'
        form.save()
        return super().form_valid(form)


class NewRentEdari(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentEdari
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'5'
        form.save()
        return super().form_valid(form)


class NewBuyColangi(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyColangi
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'6'
        form.save()
        return super().form_valid(form)


class NewSellColangi(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyColangi
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'7'
        form.save()
        return super().form_valid(form)


class NewRentColangi(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentColangi
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'8'
        form.save()
        return super().form_valid(form)


class NewBuySuit(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuySuit
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'9'
        form.save()
        return super().form_valid(form)


class NewSellSuit(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuySuit
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'10'
        form.save()
        return super().form_valid(form)


class NewRentSuit(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentSuit
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'11'
        form.save()
        return super().form_valid(form)


class NewBuyVila(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyVila
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'12'
        form.save()
        return super().form_valid(form)


class NewSellVila(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyVila
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'13'
        form.save()
        return super().form_valid(form)


class NewRentVila(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentVila
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'14'
        form.save()
        return super().form_valid(form)


class NewBuyTejari(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyTejari
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'15'
        form.save()
        return super().form_valid(form)


class NewSellTejari(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyTejari
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'16'
        form.save()
        return super().form_valid(form)


class NewRentTejari(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentTejari
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'17'
        form.save()
        return super().form_valid(form)


class NewBuyZamin(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyZamin
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'18'
        form.save()
        return super().form_valid(form)


class NewSellZamin(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyZamin
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'19'
        form.save()
        return super().form_valid(form)


class NewRentZamin(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentZamin
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'20'
        form.save()
        return super().form_valid(form)


class NewBuyBagh(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyBagh
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'21'
        form.save()
        return super().form_valid(form)


class NewSellBagh(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyBagh
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'22'
        form.save()
        return super().form_valid(form)


class NewRentBagh(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentBagh
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'23'
        form.save()
        return super().form_valid(form)


class NewBuyAnbar(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyAnbar
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'24'
        form.save()
        return super().form_valid(form)


class NewSellAnbar(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuyAnbar
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'25'
        form.save()
        return super().form_valid(form)


class NewRentAnbar(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentAnbar
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'26'
        form.save()
        return super().form_valid(form)


class NewBuySole(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuySole
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'27'
        form.save()
        return super().form_valid(form)


class NewSellSole(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = SellBuySole
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'28'
        form.save()
        return super().form_valid(form)


class NewRentSole(FormView):
    template_name = 'advertisement/new_ad.html'
    form_class = RentSole
    success_url = reverse_lazy('advertisement:advertisement_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            form.instance.published = True
        form.instance.category = u'29'
        form.save()
        return super().form_valid(form)

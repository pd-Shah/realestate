from django.views.generic import (
    ListView,
    TemplateView,
    FormView,
    DetailView,
)
from django.urls import reverse_lazy
from django.db.models import Q
from . models import Advertisement
from customer.models import CustomerProfile
from django.shortcuts import redirect
from django.urls import reverse
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

    def get_queryset(self, ):
        object_list = Advertisement.objects.filter(
            published=True).order_by('-created')
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('phone'):
            context['customer'] = CustomerProfile.objects.filter(
                phone_number=self.request.session.get('phone')
            ).first()
        return context


class SearchResultsView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Advertisement.objects.filter(
            Q(title__icontains=query) |
            Q(city__icontains=query)
        )
        return object_list


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement/advertisment_detail.html'


class AdvertisementListViewMap(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list_map.html'

    def get_queryset(self, ):
        object_list = Advertisement.objects.filter(
            published=True).order_by('-created')
        return object_list


class AboutUsView(TemplateView):
    template_name = 'advertisement/about_us.html'


class SelectAddView(TemplateView):
    template_name = 'advertisement/select.html'


class ContactUsView(TemplateView):
    template_name = 'advertisement/contact_us.html'


class MyPageView(TemplateView):
    template_name = 'advertisement/mypage.html'

    def get(self, request):
        if request.session.get('phone'):
             return redirect(reverse('advertisement:my_ads'))
        return super(MyPageView, self).get(request)


class RulePageView(TemplateView):
    template_name = 'advertisement/rules.html'


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


class BuyApartmentListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'0')



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


class SellApartmentListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'1')



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


class RentApartmentListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'2')



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


class BuyEdariListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'3')



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


class SellEdariListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'4')



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


class RentEdariListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'5')



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


class BuyColangiListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'6')



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


class SellColangiListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'7')



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


class RentColangiListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'8')



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


class BuySuitListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'9')



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


class SellSuitListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'10')



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


class RentSuitListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'11')



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


class BuyVilaListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'12')



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


class SellVilaListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'13')



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


class RentVilaListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'14')



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


class BuyTejariListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'15')



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


class SellTejariListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'16')



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


class RentTejariListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'17')



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


class BuyZaminListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'18')



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


class SellZaminListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'19')



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


class RentZaminListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'20')



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


class BuyBaghListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'21')



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


class SellBaghListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'22')



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


class RentBaghListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'23')



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


class BuyAnbarListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'24')



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


class SellAnbarListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'25')



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


class RentAnbarListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'26')



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


class BuySoleListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'27')



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


class SellSoleListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'28')



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


class RentSoleListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    queryset = Advertisement.objects.filter(category=u'29')



class TutorialTemplateView(TemplateView):
    template_name = "advertisement/tutorial.html"


class MyAdView(TemplateView):
    template_name = 'advertisement/myads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('phone'):
            context['posts'] = Advertisement.objects.filter(
            phone_number=self.request.session.get('phone')
            )
        return context


class MarkedAdView(TemplateView):
    template_name = 'advertisement/marked_ad.html'


class SimilarAdView(ListView):
    model = Advertisement
    template_name = 'advertisement/simillar_ad.html'

    def get_queryset(self):
        phone = self.request.session.get('phone')
        if phone:
            queries = Advertisement.objects.filter(phone_number=phone)
            return Advertisement.objects.filter(
                title__in=[query.title for query in queries]
                )

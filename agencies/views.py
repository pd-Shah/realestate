from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)
from django.contrib.auth import (
    login,
    authenticate,
)
from django.shortcuts import (
    render,
    redirect,
)
from django.contrib.auth.views import LoginView
from .models import Agencies
from advertisement.models import Advertisement
from .forms import SingUpForm, CustomAuthenticationForm
from django.urls import reverse_lazy


class AgenciesListView(ListView):
    model = Agencies
    template_name = 'agencies/agencies_list.html'


class AgenciesDetailView(DetailView):
    model = Agencies
    template_name = 'agencies/agencies_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range'] = range(int(self.object.popularity))
        context["posts"] = Advertisement.objects.filter(
                                owner__id=self.kwargs['pk'],
                                )
        return context


def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.agencies.urban_area_number = form.cleaned_data.get(
                                                    "urban_area_number"
                                                )
            user.agencies.address = form.cleaned_data.get("address")
            user.agencies.city = form.cleaned_data.get("city")
            user.agencies.phone_number = form.cleaned_data.get("phone_number")
            user.agencies.image = form.cleaned_data.get("image")
            user.agencies.skill = form.cleaned_data.get("skill")
            user.agencies.about_me = form.cleaned_data.get("about_me")
            user.agencies.long_description = form.cleaned_data.get("long_description")
            user.agencies.code_number = form.cleaned_data.get("code_number")
            user.agencies.web_site = form.cleaned_data.get("web_site")
            user.agencies.instagram = form.cleaned_data.get("instagram")
            user.agencies.image_owner = form.cleaned_data.get("image_owner")
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/agencies/agencies-list/')
    else:
        form = SingUpForm()
    return render(request, 'agencies/signup.html', {'form': form})


class AgenciesLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "agencies/login.html"
    success_url = reverse_lazy('agencies:my_ads')


class AgenciesAdsView(TemplateView):
    template_name = "agencies/my_add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and isinstance(self.request.user, Agencies):
            username_id = self.request.user.id
            context["posts"] = Advertisement.objects.filter(
                                    owner__id=username_id,
                                    )
        return context


class AgenciesSimillarAdsView(TemplateView):
    template_name = "agencies/similar_Ad.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            username_id = self.request.user.id
            queries = Advertisement.objects.filter(owner__id=username_id, )
            context["posts"] = Advertisement.objects.filter(
                title__in=[query.title for query in queries]
                )
        return context


class AgenciesMarkedAdsView(TemplateView):
    template_name = "agencies/marked_ad.html"


class LogingSingup(TemplateView):
    template_name = "agencies/login_or_signup.html"

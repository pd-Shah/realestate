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
from .models import Consultant
from advertisement.models import Advertisement
from .forms import SingUpForm, CustomAuthenticationForm
from django.urls import reverse_lazy


class ConsultantListView(ListView):
    model = Consultant
    template_name = 'consultant/consultant_list.html'


class ConsultantDetailView(DetailView):
    model = Consultant
    template_name = 'consultant/consultant_detail.html'

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
            user.consultant.urban_area_number = form.cleaned_data.get(
                                                    "urban_area_number"
                                                )
            user.consultant.address = form.cleaned_data.get("address")
            user.consultant.city = form.cleaned_data.get("city")
            user.consultant.phone_number = form.cleaned_data.get("phone_number")
            user.consultant.image = form.cleaned_data.get("image")
            user.consultant.skill = form.cleaned_data.get("skill")
            user.consultant.about_me = form.cleaned_data.get("about_me")
            user.consultant.long_description = form.cleaned_data.get("long_description")
            user.consultant.age = form.cleaned_data.get("age")
            user.consultant.usage = form.cleaned_data.get("long_description")
            user.consultant.job_experience = form.cleaned_data.get("usage")
            user.consultant.degree = form.cleaned_data.get("degree")
            user.consultant.agency_name = form.cleaned_data.get("agency_name")
            user.consultant.agency_number = form.cleaned_data.get("agency_number")
            user.consultant.english = form.cleaned_data.get("english")
            user.consultant.kordi = form.cleaned_data.get("kordi")
            user.consultant.arabi = form.cleaned_data.get("arabi")
            user.consultant.russion = form.cleaned_data.get("russion")
            user.consultant.french = form.cleaned_data.get("french")
            user.consultant.germany = form.cleaned_data.get("germany")
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/consultant/consultant-list/')
    else:
        form = SingUpForm()
    return render(request, 'consultant/signup.html', {'form': form})


class ConsultantLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "consultant/login.html"
    success_url = reverse_lazy('consultant:my_ads')


class ConsultantAdsView(TemplateView):
    template_name = "consultant/const_my_add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and isinstance(self.request.user, Consultant):
            username_id = self.request.user.id
            context["posts"] = Advertisement.objects.filter(
                                    owner__id=username_id,
                                    )
        return context


class ConsultantSimillarAdsView(TemplateView):
    template_name = "consultant/const_similar_Ad.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            username_id = self.request.user.id
            queries = Advertisement.objects.filter(owner__id=username_id, )
            context["posts"] = Advertisement.objects.filter(
                title__in=[query.title for query in queries]
                )
        return context


class ConsultantMarkedAdsView(TemplateView):
    template_name = "consultant/conts_marked_ad.html"


class LogingSingup(TemplateView):
    template_name = "consultant/login_or_signup.html"

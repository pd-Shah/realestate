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
from .forms import SingUpForm, CustomAuthenticationForm


class ConsultantListView(ListView):
    model = Consultant
    template_name = 'consultant/consultant_list.html'


class ConsultantDetailView(DetailView):
    model = Consultant
    template_name = 'consultant/consultant_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range'] = range(int(self.object.popularity))
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

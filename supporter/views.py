from django.views.generic import FormView
from .forms import RegisterSupporterForm
from django.urls import reverse_lazy
from .models import Supporter


class RegisterSupporterView(FormView):
    template_name = 'supporter/register.html'
    form_class = RegisterSupporterForm
    success_url = reverse_lazy("advertisement:advertisement_list")

    def form_valid(self, form):
        supporter = Supporter()
        supporter.name = form.cleaned_data.get("name")
        supporter.family = form.cleaned_data.get("family")
        supporter.phone_number = form.cleaned_data.get("phone_number")
        supporter.save()
        return super().form_valid(form)

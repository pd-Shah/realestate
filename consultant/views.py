from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)
from .models import Consultant


class ConsultantListView(ListView):
    model = Consultant
    template_name = 'consultant/consultant_list.html'
    paginate_by = 12


class ConsultantDetailView(TemplateView):
    model = Consultant
    template_name = 'consultant/consultant_detail.html'
    paginate_by = 12

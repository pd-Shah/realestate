from django.forms import ModelForm
from .models import Supporter


class RegisterSupporterForm(ModelForm):
    class Meta:
        model = Supporter
        fields = (
            "name",
            "family",
            "phone_number",
        )

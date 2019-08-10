from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
    URBANAREANUMBER,
    CITY,
)


class SingUpForm(UserCreationForm):
    urban_area_number = forms.ChoiceField(
        choices=URBANAREANUMBER,
        widget=forms.Select(),
        )
    address = forms.CharField(
        widget=forms.Textarea(),
        )
    city = forms.ChoiceField(
        choices=CITY,
        widget=forms.Select(),
    )
    phone_number = forms.CharField(
        max_length=17,
        )
    image = forms.ImageField()

    class Meta:
        model = User
        fields = (
            'username',
            "email",
            "first_name",
            "last_name",
            'password1',
            'password2',
            "urban_area_number",
            "address",
            "city",
            "phone_number",
            "image",
        )

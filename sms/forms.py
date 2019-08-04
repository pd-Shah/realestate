from django.forms import (
    Form
)
from django import forms
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{11,15}$',
    message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed."
)


class InputPhoneNumber(Form):
    phone_number = forms.CharField(
        validators=[phone_regex],
        max_length=17,
        label="شماره همراه",
        widget=forms.TextInput(
            attrs={
                "placeholder": "09226255415",
                "class": "form-control",
                "aria-label": "شماره تلفن",
                "aria-describedby": "basic-addon2",
            },
        )
    )


class InputCodeForm(Form):
    phone_number = forms.CharField(
        validators=[phone_regex],
        max_length=17,
        label="شماره همراه",
        widget=forms.TextInput(
            attrs={
                "placeholder": "09226255415",
                "class": "form-control",
                "aria-label": "شماره تلفن",
                "aria-describedby": "basic-addon2",
            },
        )
    )
    code = forms.CharField(
        label="کد",
        widget=forms.TextInput(
            attrs={
                "placeholder": "54321"
            }
        )
    )

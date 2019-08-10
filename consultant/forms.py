from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
    URBANAREANUMBER,
    CITY,
)


class SingUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "نام کاربری"
        self.fields['email'].label = "ایمیل"
        self.fields['first_name'].label = "نام"
        self.fields['last_name'].label = "نام خانوادگی"
        self.fields['password1'].label = "پسورد"
        self.fields['password2'].label = "تکرار پسورد"

    urban_area_number = forms.ChoiceField(
        choices=URBANAREANUMBER,
        widget=forms.Select(),
        label="شماره منطقه",
        )
    address = forms.CharField(
        widget=forms.Textarea(),
        label="ادرس",
        )
    city = forms.ChoiceField(
        choices=CITY,
        widget=forms.Select(),
        label="شهر",
    )
    phone_number = forms.CharField(
        max_length=17,
        label="شماره تلفن",
        )
    image = forms.ImageField(
        label="تصویر",
    )

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

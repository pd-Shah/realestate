from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import (
    URBANAREANUMBER,
    CITY,
)


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label="کلمه عبور",
        widget=forms.PasswordInput,
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

        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = User
        fields = (
            'username',
            "email",
            "first_name",
            "last_name",
            'password1',
            'password2',

        )
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
    skill = forms.CharField(
        max_length=100,
        label="تخصص",)
    about_me = forms.CharField(
        max_length=100,
        label="معرفی مختصر",
    )
    long_description = forms.CharField(
        max_length=1000,
        label="معرفی جامع",
        widget=forms.Textarea(),
    )
    image = forms.ImageField(
        label="تصویر",
    )

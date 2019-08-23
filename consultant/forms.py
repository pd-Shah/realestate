from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import (
    URBANAREANUMBER,
    CITY,
    USAGE,
    DEGREE,
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
            self.fields['english'].required = False
            self.fields['kordi'].required = False
            self.fields['arabi'].required = False
            self.fields['russion'].required = False
            self.fields['french'].required = False
            self.fields['germany'].required = False

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
        label="شماره همراه",
        )
    age = forms.IntegerField(
        label="سن",
    )
    usage = forms.ChoiceField(
        choices=USAGE,
        label="مورد استفاده",
        )
    job_experience = forms.IntegerField(
        label="سابقه کار",
    )
    degree = forms.ChoiceField(
        choices=DEGREE,
        label="مدرک تحصیلی")
    agency_name = forms.CharField(
        max_length=200,
        label="نام آژانس",
    )
    agency_number = forms.IntegerField(
        label="شماره ثابت آزانس",
    )
    english = forms.BooleanField(
        label="اشنا به زبان انگلیسی",
    )
    kordi = forms.BooleanField(
        label="اشنا به زبان کردی",
    )
    arabi = forms.BooleanField(
        label="اشنا به زبان عربی",
    )
    russion = forms.BooleanField(
        label="اشنا به زبان روسی",
    )
    french = forms.BooleanField(
        label="اشنا به زبان فرانسه",
    )
    germany = forms.BooleanField(
        label="اشنا به زبان المانی",
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

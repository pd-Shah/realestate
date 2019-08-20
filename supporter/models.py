from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed."
)


class Supporter(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="نام",
    )
    family = models.CharField(
        max_length=200,
        verbose_name="نام خانوادگی",
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
        verbose_name="شماره موبایل",
    )

from random import randint
from django.db import models
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed."
)


class Phone(models.Model):
    phone_number = models.CharField(
        unique=True,
        validators=[phone_regex],
        max_length=17,
        verbose_name='موبایل',
    )
    code = models.PositiveIntegerField(
        default=randint(10000, 99999),
    )

    def __str__(self, ):
        return str(self.phone_number)

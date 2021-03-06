from uuid import uuid4
import os
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


CATEGORY = [
    (u'0', u'House'),
    (u'1', u'Apartment'),
    (u'2', u'Duplex'),
    (u'3', u'Villa'),
]

CITY = [
    (u"1", "Tehran"),
]

URBANAREANUMBER = [
    (u'1', u'1'),
    (u'2', u'2'),
    (u'3', u'3'),
    (u'4', u'4'),
    (u'5', u'5'),
    (u'6', u'6'),
    (u'7', u'7'),
    (u'8', u'8'),
    (u'9', u'9'),
    (u'10', u'10'),
    (u'11', u'11'),
    (u'12', u'12'),
    (u'13', u'13'),
    (u'14', u'14'),
    (u'15', u'15'),
    (u'16', u'16'),
    (u'17', u'17'),
    (u'18', u'18'),
    (u'19', u'19'),
    (u'20', u'20'),
    (u'21', u'21'),
    (u'22', u'22'),
]

GENERAL = u"0"
DESIRED = u"1"
POWER = [
    (GENERAL, u"general"),
    (DESIRED, u"desired"),
]

POPULARITY = [
    (u"1", u"1"),
    (u"2", u"2"),
    (u"3", u"3"),
    (u"4", u"4"),
    (u"5", u"5"),
]

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed."
)


def get_image_path(instance, filename):
    id = uuid4()
    return os.path.join('Images', str(id), filename)


class Agencies(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    special = models.BooleanField(
        default=False,
        verbose_name='کاربر ویژه',
        )
    skill = models.CharField(
        max_length=100,
        verbose_name = "حوزه فعالیت",
        blank=True,
        null=True,
    )
    urban_area_number = models.CharField(
        max_length=2,
        choices=URBANAREANUMBER,
        verbose_name='شماره منطقه',
        )
    address = models.CharField(
        max_length=300,
        verbose_name="ادرس",
        )
    city = models.CharField(
        max_length=1,
        choices=CITY,
        verbose_name="شهر",
        )
    popularity = models.CharField(
        max_length=1,
        choices=POPULARITY,
        verbose_name="محبوبیت",
        default=u"5",
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ساخت اکانت",
        )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="اخرین به روز رسانی",
        )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        unique=True,
        verbose_name="شماره موبایل",
    )
    code_number = models.CharField(
        max_length=100,
        verbose_name = "شناسه صنفی ",
        blank=True,
        null=True,
    )
    web_site = models.URLField(
        verbose_name="وب سایت",
        blank=True,
        null=True,
    )
    instagram = models.URLField(
        verbose_name="ادرس اینستاگرام",
        blank=True,
        null=True,
    )
    about_me = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="معرفی",
    )
    long_description = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="معرفی جامع",
    )
    image = models.ImageField(
                        upload_to=get_image_path,
                        blank=True,
                        null=True,
                        verbose_name="تصویر آژانس",
                    )
    image_owner = models.ImageField(
                        upload_to=get_image_path,
                        blank=True,
                        null=True,
                        verbose_name="تصویر مدیران و همکاران",
                    )
    agencies = models.BooleanField(
        default=False,
    )


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_agencies_profile(sender, instance, created, **kwargs):
    if created:
        Agencies.objects.create(user=instance)
    instance.agencies.save()

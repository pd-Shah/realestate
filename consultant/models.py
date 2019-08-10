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
    (u"0", u"0"),
    (u"1", u"1"),
    (u"2", u"2"),
    (u"3", u"3"),
    (u"4", u"4"),
]

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed."
)


def get_image_path(instance, filename):
    id = uuid4()
    return os.path.join('Images', str(id), filename)


class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    special = models.BooleanField(default=False)
    urban_area_number = models.CharField(max_length=2, choices=URBANAREANUMBER)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=1, choices=CITY)
    popularity = models.CharField(max_length=1, choices=POPULARITY)
    commission_rate = models.IntegerField(
                blank=True,
                null=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        unique=True,
    )
    image = models.ImageField(
                        upload_to=get_image_path,
                        blank=True,
                        null=True,
                    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Consultant.objects.create(user=instance)
    instance.consultant.save()

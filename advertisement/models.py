import os
from uuid import uuid4
from django.db import models
from django.core.validators import RegexValidator

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


class AdvertisementImage(models.Model):
    advertisement = models.ForeignKey(
                        "Advertisement",
                        on_delete=models.CASCADE,
                    )
    image = models.ImageField(
                        upload_to=get_image_path,
                        blank=True,
                        null=True,
                    )

    def __str__(self):
        return str(self.id)


class Advertisement(models.Model, ):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    year_of_construction = models.DateField()
    room_number = models.PositiveSmallIntegerField()
    house_square = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=1, choices=CATEGORY)
    urban_area_number = models.CharField(max_length=2, choices=URBANAREANUMBER)
    published = models.BooleanField()
    publish_review = models.CharField(max_length=600, null=True, blank=True)
    consultants_number_allowed = models.SmallIntegerField(default=10)
    allowed_capture_days = models.DurationField(default=10)
    allowed_ad_days = models.DurationField(default=5)
    special = models.BooleanField(default=False)
    city = models.CharField(max_length=1, choices=CITY)
    popularity = models.CharField(max_length=1, choices=POPULARITY)
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.title

from django.contrib import admin
from django.utils.html import mark_safe
from . import models
from django.contrib.auth.models import User
from agencies.models import Agencies
from consultant.models import Consultant


for user in User.objects.all():
    Agencies.objects.get_or_create(user=user)
    Consultant.objects.get_or_create(user=user)

@admin.register(models.ConfigAdvertisement)
class AdvertismentConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Advertisement)
class AdvertismentAdmin(admin.ModelAdmin):
    list_filter = (
        "created",
        "year_of_construction",
        "room_number",
        "house_square",
        "category",
        "urban_area_number",
        "published",
        "special",
        "city",
        "popularity",
         )
    readonly_fields = ["image1_shot", "image2_shot", "image3_shot"]

    def image1_shot(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image1.url,
                width=250,
                height=250,
            ))

    def image2_shot(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image2.url,
                width=250,
                height=250,
            ))

    def image3_shot(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image3.url,
                width=250,
                height=250,
            ))

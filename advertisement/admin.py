from django.contrib import admin
from django.utils.html import mark_safe
from . import models


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
        "publish_review",
        "special",
        "phone_number",
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

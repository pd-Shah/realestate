from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.AdvertisementImage)
class AdvertismentImageAdmin(admin.ModelAdmin):
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=250,
                height=250,
            ))


class AdvertisementImageAdminInline(admin.TabularInline):
    model = models.AdvertisementImage


@admin.register(models.Advertisement)
class AdvertismentAdmin(admin.ModelAdmin):
    list_filter = (
        "title",
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
    readonly_fields = ["headshot_image"]
    inlines = (AdvertisementImageAdminInline, )

    def headshot_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=250,
                height=250,
            ))

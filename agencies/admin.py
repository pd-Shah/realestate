from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Agencies)
class Agencies(admin.ModelAdmin):
    readonly_fields = ["headshot_image"]
    list_filter = (
        "phone_number",
        "special",
        "urban_area_number",
        "city",
        "popularity",
        "created",
    )

    def headshot_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=250,
                height=250,
            ))

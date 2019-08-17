
from django.contrib import admin
from . import models


@admin.register(models.Supporter)
class Supporter(admin.ModelAdmin):
    pass

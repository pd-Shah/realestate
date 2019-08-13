from django.db import models
from advertisement.models import Advertisement


class FavoriteAd():
    class Meta:
        unique_together = ('phone_number', 'advertisement_id', )

    phone_number = models.CharField(
        max_length=17,
        verbose_name="شماره تلفن",
    )
    advertisement_id = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        verbose_name="شماره اگهی",
    )

    @staticmethod
    def set_phone_ad(phone_number, advertisement_id):
        favorite = FavoriteAd.objects.Create(
            phone_number=phone_number,
            advertisement_id=advertisement_id,
            )
        favorite.save()

    @staticmethod
    def remove_phone_add(phone_number, advertisement_id):
        FavoriteAd.objects.filter(
            phone_number=phone_number,
            advertisement_id=advertisement_id
        ).first().delete()

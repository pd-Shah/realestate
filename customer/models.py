from django.db import models
from advertisement.models import Advertisement


class CustomerProfile(models.Model):
    phone_number = models.CharField(
        max_length=17,
        verbose_name="شماره تلفن",
    )
    favorites = models.ManyToManyField(
        Advertisement,
    )

    @staticmethod
    def set_fav(phone_number, ad_id):
        ad = Advertisement.objects.get(pk=ad_id)
        customer = CustomerProfile.object.get(phone_number=phone_number)
        if customer is None:
            customer = CustomerProfile.objects.create(
                phone_number=phone_number,
            )
            customer.save()
        customer.favorites.add(ad)

    @staticmethod
    def set_unfav(phone_number, ad_id):
        ad = Advertisement.objects.get(pk=ad_id)
        customer = CustomerProfile.object.get(phone_number=phone_number)
        if customer:
            customer.favorites.remove(ad)

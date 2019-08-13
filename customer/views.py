from django.http import HttpResponse
from django.shortcuts import redirect
from .models import FavoriteAd


def set_phone_ad_view(request, advertisement_id):
    phone = request.session.get('phone')
    if phone:
        FavoriteAd.set_phone_ad(phone, advertisement_id, )
        return HttpResponse("set successfully")
    return redirect("/sms/")


def remoev_phone_ad_view(request, advertisement_id):
    phone = request.session.get('phone')
    if phone:
        FavoriteAd.remove_phone_add(phone, advertisement_id, )
        return HttpResponse("delete successfully")
    return redirect("/sms/")

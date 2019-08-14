from django.http import JsonResponse
from .models import CustomerProfile


def set_fav_view(request, advertisement_id):
    phone = request.session.get('phone')
    if phone:
        CustomerProfile.set_fav(phone, advertisement_id, )
    return JsonResponse({"success": True}, status=200)


def set_unfav_view(request, advertisement_id):
    phone = request.session.get('phone')
    if phone:
        CustomerProfile.set_unfav(phone, advertisement_id, )
    return JsonResponse({"success": True}, status=200)

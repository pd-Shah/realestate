from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('superuser/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('advertisement.urls', namespace='advertisement')),
    path('sms/', include('sms.urls', namespace='sms')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('consultant/', include('consultant.urls', namespace='consultant', )),
    path('agencies/', include('agencies.urls', namespace='agencies', )),
    path('customer/', include('customer.urls', namespace='customer', )),
    path('supporter/', include('supporter.urls', namespace='supporter', )),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

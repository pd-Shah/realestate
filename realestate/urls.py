from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('advertisement.urls', namespace='advertisement')),
    path('sms/', include('sms.urls', namespace='sms')),
    path("blog/", include("pinax.blog.urls", namespace="pinax_blog")),
    path("ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

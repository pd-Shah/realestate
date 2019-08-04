from django.urls import path
from .views import (
    BlogDetailView,
    BlogListView,
)

app_name = "blog"
urlpatterns = [
    path('', BlogListView.as_view(), name="blog_list_view", ),
    path('blog/', BlogDetailView.as_view(), name="blog_detail_view", )
]

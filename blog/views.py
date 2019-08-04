from django.views.generic import TemplateView


class BlogListView(TemplateView):
    template_name = 'blog/blog.html'


class BlogDetailView(TemplateView):
    template_name = 'blog/detail_blog.html'

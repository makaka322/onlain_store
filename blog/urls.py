from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListViews, BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path("blog_list/", BlogListViews.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog_create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog_delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog_update/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





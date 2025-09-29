from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse

from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class BlogListViews(ListView):
    model = Blog
    template_name = "blog_list.html"
    paginate_by = 3


    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ["title", "photo", "content", "is_published"]
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.add_blog"


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.delete_blog"


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ["title", "photo", "content", "is_published"]
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.change_blog"

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])
